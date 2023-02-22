'''
The script aims to parse HTML elements for PASDA(https://www.pasda.psu.edu) 
and extract parsed content into a local CSV.


Files
-----
pasdaURLs.csv
	A local csv file stores existing urls that are prepared to parse.
output_yyyymmdd.csv
	The output file after parsing and it is followed by the action date.


Developers
----------
Original created on xxxxx
Created by Karen Majewicz  @karenmajewicz

Updated December 14, 2020
Updated by Ziying Cheng  @Ziiiiing

Updated Nov 10, 2022
by @karenmajewicz
Adds landing page and full metadata link

Updated Feb 5, 2023
by ardumn
Addtional comments

'''

import csv # The csv module implements classes to read and write tabular data in CSV format.
import time # This module provides various time-related functions.
import urllib.request # The urllib.request module defines functions and classes which help in opening URLs (mostly HTTP)
from bs4 import BeautifulSoup # For pulling data out of HTML and XML files

# extract exising urls from local csv file

urls = [] # Creates a container for URLs to be generated

# reads the rows from the output CSV from datasetURL.py

with open(' .csv') as fr: # Opens CSV file
    reader = csv.reader(fr)  # Reader object assigned
    for row in reader: # Scans each URL to be appended 
        urls.append(row) # Appended to each row


# store parsed elements for all urls

parseElements = [] # Generates parsed elements for URLs to be stored (similar to above)

for url in urls:
	landingPage = str(url) # Creates the landing page based on URL extracted
	page = urllib.request.urlopen(url[0]).read() # Basic webpage generated from URL parsed
	soup = BeautifulSoup(page, "html.parser") # Pulling data from HTML Parser

	titleField = soup.find(attrs={'id': 'Label1'}) # Finds attributes in relation to title field and is labeled
	dateField = soup.find(attrs={'id': 'Label2'})  # Finds attributes in relation to date field and is labeled
	publisherField = soup.find(attrs={'id': 'Label3'}) # Finds attributes in relation to publisher field and is labeled
	descriptionField = soup.find(attrs={'id': 'Label14'}) # Finds attributes in relation to description field and is labeled
	metadataLink = soup.find('a', href=True, text='Metadata') # Finds attributes in relation to metadata field and is labeled
	downloadLink = soup.find('a', href=True, text='Download') # Finds attributes in relation to download field and is labeled

# Stripped fields if above parameters fail

	title = titleField.text.strip() # Stripped if BeautifulSoup module fails or slips through
	date = dateField.text.strip() # Stripped if BeautifulSoup module fails or slips through
	publisher = publisherField.text.strip() # Stripped if BeautifulSoup module fails or slips through
	description = descriptionField.text.strip() # Stripped if BeautifulSoup module fails or slips through
	metadata = "https://www.pasda.psu.edu/uci/" + metadataLink['href'] # Stripped if BeautifulSoup module fails or slips through
	try:
		download = downloadLink['href'] # Resort to different download link if cannot find a suitable field to fill
	except:
		download = 'nil'
		
	# Default Values (Assigned default values for resource class)
    
	code = '08a-01'  # Portal Hub Header
	accessRights = "Public" # Access Rights Header
	accrualMethod = "HTML" # Accrual Method Header
	dateAccessioned = time.strftime('%Y-%m-%d') # Data Accessioned Header
	language = "eng" # Language Header
	isPartOf = "08a-01" # Part of Portal Header
	memberOf = "ba5cc745-21c5-4ae9-954b-72dd8db6815a" # Member of Link Header
	provider = "Pennsylvania Spatial Data Access (PASDA)" # Provider Agency Header
	resourceClass = "" # Resource Class Header
	resourceType = '' # Resource Type Header
	dateRange = '' # Date Range Header
	slug = landingPage.rsplit('=', 1)[-1] # Landing Page Header
	iden = "pasda-" + slug # Main Identifier

    
	parseElements.append([landingPage,iden,title,date,dateRange,publisher,provider,language,description,resourceClass,resourceType,metadata,download,code,isPartOf,memberOf,accessRights,accrualMethod,dateAccessioned])
    
    
# Generate action date with format YYYYMMDD

actionDate = time.strftime('%Y%m%d')

# Write outputs to local CSV file

with open(f'output_{actionDate}.csv', 'w') as fw: # Concatinates Fields
	fields = ['Information','Identifier','Title','Temporal Coverage','Date Range','Publisher','Provider','Language','Description','Resource Class','Resource Type','HTML','Download','Code','Is Part Of','Member Of','Access Rights','Accrual Method','Date Accessioned']

	writer = csv.writer(fw)           # Writes 
	writer.writerow(fields)           # Field Names
	writer.writerows(parseElements)   # Elements

	print('#### Job done ####')
	
	


