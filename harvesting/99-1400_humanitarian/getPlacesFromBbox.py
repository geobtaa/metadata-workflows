import pandas as pd
import requests
import time

# Define function to reverse-geocode a bounding box
def reverse_geocode(bbox):
    # Define the API endpoint URL
    url = f"https://nominatim.openstreetmap.org/reverse?format=jsonv2&bounded=1&polygon_geojson=1&limit=1&{bbox}"

    # Make the API request
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        if "error" not in data:
            # Return the place name
            return data.get("display_name")
        else:
            print(f"Error: {data.get('error')}")
    else:
        print(f"Error: {response.status_code}")

    # Wait for 1 second before making the next request
    time.sleep(1)

# Read bounding boxes from a CSV file
data = pd.read_csv("bbox-no-place.csv")

# Reverse-geocode each bounding box and store the results in a new list
places = []
for i, row in data.iterrows():
    bbox = row["bbox"]
    place = reverse_geocode(bbox)
    places.append(place)

# Add the extracted places to the dataframe
data["Place"] = places

# Save the results to a new CSV file
data.to_csv("output.csv", index=False)
