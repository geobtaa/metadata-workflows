# PASDA 08a-01
About harvesting metadata records from the PASDA data portal

## Overview of PASDA
[Pennsylvania Spatial Data Access (PASDA)](https://www.pasda.psu.edu) is the state’s comprehensive GIS clearinghouse. Most Pennsylvania statewide agencies and regional organizations provide their data through this site. Many counties and cities do as well.

## How to harvest metadata records from PASDA

### Part 1: Scrape the PASDA portal
1. Use the script `datasetURLs.py` to obtain a list of all of the records currently in PASDA. The resulting CSV will be called `pasdaURLS_{today's date}.csv` which is just a list of the landing pages for the datasets in the PASDA portal.


2. Use the `pasdaURLS_{today's date}.csv` and the `html2csv.py`script to scrape the metadata from the PASDA landing pages. This resulting CSV will be called `output_{today's date}.csv`.


