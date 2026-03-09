import os
import pymupdf

from dotenv import load_dotenv
from pathlib import Path

from src.data_preparation.text_cleaning import TextProcessor
from src.data_preparation.ingest import chunk_doc
from src.schemas.type_models import SourceDocument


load_dotenv()

file_ = os.getenv("OWNER_FILE_PATH")
if file_ is None:
    raise RuntimeError("OWNER_FILE_PATH environment variable is not set")

owner_doc = SourceDocument(
    filename="owner_manual",
    filepath=Path(file_),
    page_count=597,
    start_page=10,
    end_page=-20,
)

doc = pymupdf.open(owner_doc.filepath)


tp_replace = {"‘‘": '"', "’’": '"', "‘": "'", "’": "'", "\n": " "}
tp_removal = (r"\(\d+\)",)
tp_udfs = (lambda x: x[:-91],)

tp = TextProcessor(udfs=tp_udfs)

skip_map = {"*": 5, "(P.": 3, ".": 20}

chunks = chunk_doc(
    owner_doc,
    tp,
)

# for i, page in enumerate(doc):
#     text = page.get_text()
#     print(text)

#     if i == 10:
#         break

# print(type(doc[321]))
# print(str(doc[50].get_text()))
# print(tp.clean(str(doc[50].get_text())))
# print(doc[321].get_text("blocks"))
# print(doc[6].get_text().count("(P."))
print(doc.page_count)
# print(ord("‘"))
