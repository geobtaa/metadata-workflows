# PASDA 08a-01
About harvesting metadata records from the PASDA data portal

## Overview of PASDA
[Pennsylvania Spatial Data Access (PASDA)](https://www.pasda.psu.edu) is the state’s comprehensive GIS clearinghouse. Most Pennsylvania statewide agencies and regional organizations provide their data through this site. Many counties and cities do as well.

## How to harvest metadata records from PASDA

### Part 1: Scrape the PASDA portal
1. Use the script `datasetURLs.py` to obtain a list of all of the records currently in PASDA. The resulting CSV will be called `pasdaURLS_{today's date}.csv` which is just a list of the landing pages for the datasets in the PASDA portal.


2. Use the `pasdaURLS_{today's date}.csv` and the `html2csv.py`script to scrape the metadata from the PASDA landing pages. This resulting CSV will be called `output_{today's date}.csv`.


### Part 2: Extract the bounding boxes
Context: most of the records have supplemental metadata in ISO 19139 or FGDC format. The link to this document is found in the 'Metadata" column.
Although these files are created as XMLs, the link is a rendered HTML.

1. Create a CSV file that is a list of just the metadata file pages. See sample-inputMetadataUrls.csv for an example.

2. Use the getBbox.py script to parse the files and extract the bounding boxes.
3. Merge these values back into the output CSV from Part 1.


