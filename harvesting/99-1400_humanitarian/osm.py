import pandas as pd
import requests

# Define function to geocode a place name using Nominatim API
def geocode_place_name(place_name):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": place_name,
        "format": "jsonv2"
    }
    response = requests.get(url, params=params)
    if response.ok:
        data = response.json()
        if len(data) > 0 and "boundingbox" in data[0]:
            bbox = data[0]["boundingbox"]
            return [bbox[2], bbox[0], bbox[3], bbox[1]]
    return None

# Load the CSV file into a pandas dataframe
df = pd.read_csv("All_Metadata.csv")

# Apply the geocode_place_name function to the "Spatial Coverage" column
df["bbox"] = df["Spatial Coverage"].apply(geocode_place_name)

# Write the results to a new CSV file
df.to_csv("output.csv", index=False)