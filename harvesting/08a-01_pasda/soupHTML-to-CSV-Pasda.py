'''
The script aims to parse HTML elements for PASDA(https://www.pasda.psu.edu) 
and extract parsed content into a local CSV. The progress is maintained on GitHub
(https://github.com/BTAA-Geospatial-Data-Project/parse-html).


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

'''

import csv
import time
import urllib.request
from bs4 import BeautifulSoup

# extract exising urls from local csv file
urls = []

with open('pasdaURLs.csv') as fr:
    reader = csv.reader(fr)  # reader object
    for row in reader:
        urls.append(row)


# store parsed elements for all urls
parseElements = []

for url in urls:
    page = urllib.request.urlopen(url[0]).read()
    soup = BeautifulSoup(page, "html.parser")
    print(f'Parsing {url[0]}')

    titleField = soup.find(attrs={'id': 'Label1'})
    dateField = soup.find(attrs={'id': 'Label2'})
    publisherField = soup.find(attrs={'id': 'Label3'})
    descriptionField = soup.find(attrs={'id': 'Label14'})
    metadataLink = soup.find('a', href=True, text='Metadata')
    # downloadLink = soup.find('a', href=True, text='Download')

    title = titleField.text.strip()
    #title2 = titleField.get_text()
    date = dateField.text.strip()
    publisher = publisherField.text.strip()
    description = descriptionField.text.strip()
    metadata = metadataLink['href']
    # download = downloadLink['href']
    
    parseElements.append([title,date,publisher,description,metadata])
    
    
# generate action date with format YYYYMMDD
actionDate = time.strftime('%Y%m%d')

# write outputs to local csc file
with open(f'output_{actionDate}.csv', 'w') as fw:
    fields = ['Title','Date','Publisher','Description','Metadata']
    
    writer = csv.writer(fw)   
    writer.writerow(fields)           # fieldnames
    writer.writerows(parseElements)   # elements

    print('#### Job done ####')


