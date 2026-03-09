import pymupdf

from collections.abc import Mapping
from enum import Enum
from typing import Any, Generator

from src.data_preparation.text_cleaning import TextProcessor
from src.schemas.type_models import SourceDocument, TextChunk


class ChunkOptions(Enum):
    PAGE = "text"
    PARAGRAPH = "blocks"
    WORD = "words"


def skip_content_dynamic(text: str, rules: Mapping[str, int | float]) -> bool:
    """
    Sometimes there's a number of unwanted characters in the page
    that makes skipping page a better option. In other cases, some undesired pages
    (e.g. list of contents) are showing patters that are skippable.

    :param text: Text from processed page
    :type text: str
    :param rules: Rules provided in tuple format with first element being a pattern substring
                and second being the threshold that will trigger skipping.
                Example (".", 100) -> skip page if there's more than 100 dots in it.
    :type rules: list[tuple[str, int | float]]
    :return: Skippable yes/no
    :rtype: bool
    """
    return any(text.count(substr) > threshold for substr, threshold in rules.items())


def extract_chunk(page: pymupdf.Page, chunk_type: ChunkOptions) -> list[Any]:
    if chunk_type == ChunkOptions.PAGE:
        text = page.get_text("text")
        return [text] if isinstance(text, str) else []
    else:
        chunks = page.get_text(chunk_type.value)
        return chunks if isinstance(chunks, list) else []


def chunk_doc(
    source: SourceDocument,
    processor: TextProcessor,
    chunk_type: ChunkOptions = ChunkOptions.PAGE,
    skip_rules: Mapping[str, int | float] = {},
) -> Generator[TextChunk, None, None]:
    doc = pymupdf.open(source.filepath)

    page_id = 1
    chunk_id = 1
    for page in doc:
        for chunk in extract_chunk(page, chunk_type):

            if chunk_type == ChunkOptions.PAGE and skip_content_dynamic(
                chunk, skip_rules
            ):
                continue

            clean_text = processor.clean(chunk)

            # Should I do the embeddings here?

            yield TextChunk(
                id=chunk_id,
                document_id=source.id,
                text=clean_text,
                page_number=page_id,
                embedding=[1, 1],
            )

        chunk_id += 1
