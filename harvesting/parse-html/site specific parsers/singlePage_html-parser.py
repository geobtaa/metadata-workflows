# import libraries
import urllib2
from bs4 import BeautifulSoup
import csv
from datetime import datetime


# specify the url
quote_page = 'http://www.pasda.psu.edu/uci/DataSummary.aspx?dataset=1203'

# query the website and return the html to the variable 'page'
page = urllib2.urlopen(quote_page)

# parse the html using beautiful soap and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

# Take out the <div> of name and get its value
titleField = soup.find(attrs={'id': 'Label1'})
dateField = soup.find(attrs={'id': 'Label2'})
publisherField = soup.find(attrs={'id': 'Label3'})
descriptionField = soup.find(attrs={'id': 'Label14'})
metadataLink = soup.find('a', href=True, text='Metadata')
downloadLink = soup.find('a', href=True, text='Download')






 # strip() is used to remove starting and trailing
Title = titleField.text.strip(),
Date = dateField.text.strip(),
Publisher = publisherField.text.strip(),
Description = descriptionField.text.strip(),
Metadata = metadataLink['href'],
Download = downloadLink['href']




# print name

# open a csv file with append, so old data will not be erased
with open('index.csv', 'a') as csv_file:
	writer = csv.writer(csv_file)
	writer.writerow([Title,Date,Publisher,Description,Metadata,Download])