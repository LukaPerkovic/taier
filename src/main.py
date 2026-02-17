import os

from dotenv import load_dotenv

import pymupdf

# from src.data_preparation.text_cleaning import TextProcessor


load_dotenv()

file_ = os.getenv("OWNER_FILE_PATH")

doc = pymupdf.open(file_)

# for i, page in enumerate(doc):
#     text = page.get_text()
#     print(text)

#     if i == 10:
#         break

print(type(doc[321]))
# print(doc[321].get_text()[:-90])
# print(doc[321].get_text("blocks"))
# print(doc[6].get_text().count("(P."))
# print(ord("‘"))
