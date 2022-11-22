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

'''

import csv
import time
import urllib.request
from bs4 import BeautifulSoup
# extract exising urls from local csv file
urls = []

## read the rows from the output CSV from datasetURL.py
with open(' .csv') as fr:
    reader = csv.reader(fr)  # reader object
    for row in reader:
        urls.append(row)


# store parsed elements for all urls
parseElements = []

for url in urls:
	landingPage = str(url)
	page = urllib.request.urlopen(url[0]).read()
	soup = BeautifulSoup(page, "html.parser")

	titleField = soup.find(attrs={'id': 'Label1'})
	dateField = soup.find(attrs={'id': 'Label2'})
	publisherField = soup.find(attrs={'id': 'Label3'})
	descriptionField = soup.find(attrs={'id': 'Label14'})
	metadataLink = soup.find('a', href=True, text='Metadata')
	downloadLink = soup.find('a', href=True, text='Download')

	title = titleField.text.strip()
	date = dateField.text.strip()
	publisher = publisherField.text.strip()
	description = descriptionField.text.strip()
	metadata = "https://www.pasda.psu.edu/uci/" + metadataLink['href']
	try:
		download = downloadLink['href']
	except:
		download = 'nil'
		
	#default values
	code = '08a-01'
	accessRights = "Public"
	accrualMethod = "HTML"
	dateAccessioned = time.strftime('%Y-%m-%d')
	language = "eng"
	isPartOf = "08a-01"
	memberOf = "ba5cc745-21c5-4ae9-954b-72dd8db6815a"
	provider = "Pennsylvania Spatial Data Access (PASDA)"
	resourceClass = ""
	resourceType = ''
	dateRange = ''
	slug = landingPage.rsplit('=', 1)[-1]
	iden = "pasda-" + slug

    
	parseElements.append([landingPage,iden,title,date,dateRange,publisher,provider,language,description,resourceClass,resourceType,metadata,download,code,isPartOf,memberOf,accessRights,accrualMethod,dateAccessioned])
    
    
# generate action date with format YYYYMMDD
actionDate = time.strftime('%Y%m%d')

# write outputs to local csc file
with open(f'output_{actionDate}.csv', 'w') as fw:
	fields = ['Information','Identifier','Title','Temporal Coverage','Date Range','Publisher','Provider','Language','Description','Resource Class','Resource Type','HTML','Download','Code','Is Part Of','Member Of','Access Rights','Accrual Method','Date Accessioned']

	writer = csv.writer(fw)   
	writer.writerow(fields)           # fieldnames
	writer.writerows(parseElements)   # elements

	print('#### Job done ####')
	
	


