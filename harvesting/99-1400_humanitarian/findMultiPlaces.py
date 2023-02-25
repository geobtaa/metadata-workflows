import spacy
import pandas as pd

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

# Read data from CSV file
data = pd.read_csv("missing-spatial-coverage.csv")

# Extract place names from each title and description
places = []
for i, row in data.iterrows():
    title = row["Title"]
    desc = row["Description"]
    place_names = extract_place_names(title)
    if not place_names:
        place_names = extract_place_names(desc)
    places.append("|".join(place_names))

# Add the extracted places to the dataframe
data["Place"] = places

# Save the results to a new CSV file
data.to_csv("output.csv", index=False)
