import spacy
import csv

# Load English language model for spaCy
nlp = spacy.load("en_core_web_sm")

# Define function to extract place names from a text
def extract_place_names(text):
    doc = nlp(text)
    place_names = []
    for ent in doc.ents:
        if ent.label_ == "GPE": # GPE is the label for geopolitical entities, i.e. place names
            place_names.append(ent.text)
    return place_names

# Read titles from a file
with open("titles.txt", "r") as file:
    titles = file.readlines()

# Open output CSV file
with open("places.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Write header row
    writer.writerow(["Title", "Place"])

    # Write data rows
    for title in titles:
        title = title.strip()
        place_names = extract_place_names(title)
        for place in place_names:
            writer.writerow([title, place])