import xml.etree.ElementTree as ET
import csv

# Load XML file
tree = ET.parse('oai-pmh.xml')
root = tree.getroot()

# Open CSV file
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Write header row
    header = []
    for child in root[0]:
        header.append(child.tag)
    writer.writerow(header)

    # Write data rows
    for elem in root:
        row = []
        for child in elem:
            row.append(child.text)
        writer.writerow(row)
