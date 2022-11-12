#This script is to use Pandas to parse websites that have the metadata in tables

# import libraries
import csv
import re
from urllib.request import urlopen
import pandas as pd
from bs4 import BeautifulSoup

#declare empty list
contents = []

#create a name for a new CSV to be written
f = csv.writer(open('xx.csv', 'w'))
# f.writerow(['Title','Date','Publisher','Description','Download'])

#add the name of a csv that is just a list of URLs to be parsed
with open('yy.csv','r') as csvf: # Open file in read mode
    urls = csv.reader(csvf)
    for url in urls:
        contents.append(url) # Add each url to list contents

for url in contents:  # Parse through each url in the list and find tables
	page = urlopen(url[0]).read()
	soup = BeautifulSoup(page, "html.parser")
	table = soup.find('table')
	table_rows = table.find_all('tr')

	for tr in table_rows:
		td = tr.find_all('td')
		row = [tr.text for tr in td]
		print(row)















