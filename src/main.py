import os
import pymupdf

from dotenv import load_dotenv
from pathlib import Path

from src.schemas.type_models import SourceDocument

load_dotenv()

file_owner = os.getenv("OWNER_FILE_PATH")
file_service = os.getenv("SERVICE_FILE_PATH")
if not file_owner or not file_service:
    raise RuntimeError("Document environment variables are not set")

owner_doc = SourceDocument(
    filename="owner_manual",
    filepath=Path(file_owner),
    start_page=10,
    end_page=-20,
)


service_doc = SourceDocument(
    filename="service_manual", filepath=Path(file_service), start_page=10
)

doc = pymupdf.open(owner_doc.filepath)


# tp_replace = {"‘‘": '"', "’’": '"', "‘": "'", "’": "'", "\n": " "}
# tp_removal = (r"\(\d+\)",)
# tp_udfs = (lambda x: x[:-91],)

# tp = TextProcessor(replace=tp_replace, remove=tp_removal, udfs=tp_udfs)

# skip_map = {"*": 5, "(P.": 3, ".": 20}


# from time import time

# chunking_start = time()
# chunks = chunk_doc(owner_doc, tp, skip_rules=skip_map)

# k = 0
# for ch in chunks:
#     print(ch.text.count("*"))
# chunking_end = time()

# print(chunking_end - chunking_start)
# for i, page in enumerate(doc):
#     text = page.get_text()
#     print(text)

#     if i == 10:
#         break

# print(type(doc[321]))
# print(str(doc[10].get_text()))
# print(tp.clean(str(doc[50].get_text())))
# print(doc[321].get_text("blocks"))
# print(doc[6].get_text().count("(P."))
# print(doc.page_count)
# print(ord("‘"))
