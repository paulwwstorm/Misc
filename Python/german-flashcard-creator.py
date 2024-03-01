import pandas as pd
from docx import Document

file_path = str("C:/Users/anapa/OneDrive/OneDrive文稿/Learning/Misc/Language/Deutsch/Wordlists/Anki cards.docx")

# f = open(file_path, encoding="rb")
doc = Document(file_path)

flashcard_unformatted = []

for para in doc.paragraphs:
    flashcard_unformatted.append(para.text)

flashcards_formatted = ()

current_part = ""

for x in range(len(flashcard_unformatted)):
    print(x)

# for x in range(100):
#     if (flashcard_unformatted[x] == "#") and (flashcard_unformatted[x + 4] == "#"):
#         print("---")
#     elif (flashcard_unformatted[x] == "#") and (flashcard_unformatted[x + 2] == "#"):
#         print(current_part)
#     else:
#         current_part += flashcard_unformatted[x]

