import csv
import re
import urllib2
import csv
from urllib2 import urlopen

from bs4 import BeautifulSoup

portalMetadata = []

f = csv.writer(open('pasda_20190904.csv', 'w'))
f.writerow(['Title','Date','Publisher','Description','Metadata'])

with open('pas.csv','r') as harvest:
    urls = csv.reader(harvest)
    for url in urls:
        portalMetadata.append(url)

for url in contents:
	page = urlopen(url[0]).read()
	soup = BeautifulSoup(page, "html.parser")

	titleField = soup.find(attrs={'id': 'Label1'})
	dateField = soup.find(attrs={'id': 'Label2'})
	publisherField = soup.find(attrs={'id': 'Label3'})
	descriptionField = soup.find(attrs={'id': 'Label14'})
	metadataLink = soup.find('a', href=True, text='Metadata')


	title = titleField.text.strip(),
	date = dateField.text.strip(),
	publisher = publisherField.text.strip(),
	description = descriptionField.text.strip(),
	metadata = metadataLink['href'],


	f.writerow([title,date,publisher,description,metadata])
















