import pandas as pd
from docx import Document
import anki
import genanki
from random import random

word_doc_name = "Intermediate Cards 3"
collection_name = "German Vocab::Intermediate 3"
card_type = "German Vocab"

print("generating flaschards")

file_path = str("C:/Users/anapa/OneDrive/OneDrive文稿/Learning/Misc/Language/Deutsch/Wordlists/Intermediate Cards 3.docx")

# f = open(file_path, encoding="rb")
doc = Document(file_path)

flashcard_unformatted = []

for para in doc.paragraphs:
    flashcard_unformatted.append(para.text)

flashcard_unformatted = str(flashcard_unformatted[0])

column_names = ["German","中文","Example"]
flashcards_formatted = pd.DataFrame(columns=column_names)
current_card = []
current_part = ""

german_intermediate_3 = genanki.Deck(
    20240528,
    collection_name
  )

german_vocab_model = genanki.Model(
  2024052802,
  'German Intermediate',
  fields=[
    {'name': 'German'},
    {'name': '中文'},
    {'name': 'Example'},
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{中文}}',
      'afmt': '{{German}}<hr id="answer">{{Example}}',
    },
  ])

for x in range(len(flashcard_unformatted)):
    if (flashcard_unformatted[x] == "*" and current_part != ""):
        current_card.append(current_part)
        print("current_part:" + current_part)
        flashcards_formatted.loc[len(flashcards_formatted)] = current_card
        note = genanki.Note(
            model=german_vocab_model,
            fields=[current_card[0], current_card[1], current_card[2]])
        german_intermediate_3.add_note(note)
        current_part = ""
        current_card = []
    elif (flashcard_unformatted[x] == "#"):
        current_card.append(current_part)
        current_part = ""
    else:
        current_part += flashcard_unformatted[x]

genanki.Package(german_intermediate_3).write_to_file('output.apkg')

        

