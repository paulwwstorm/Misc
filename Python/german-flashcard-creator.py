import pandas as pd
from docx import Document

file_path = str("C:/Users/anapa/OneDrive/OneDrive文稿/Learning/Misc/Language/Deutsch/Wordlists/Anki cards.docx")

# f = open(file_path, encoding="rb")
doc = Document(file_path)

flashcard_unformatted = []

for para in doc.paragraphs:
    flashcard_unformatted.append(para.text)

flashcard_unformatted = str(flashcard_unformatted[0])

flashcards_formatted = 

current_part = ""

for x in range(len(flashcard_unformatted)):
    if (flashcard_unformatted[x] == "*"):
        print(current_part)
        current_part = ""
        print("\n")
        print("New entry found")
        print("---")
    elif (flashcard_unformatted[x] == "#"):
        print(current_part)
        current_part = ""
    else:
        current_part += flashcard_unformatted[x]
        

