# import libraries

import csv
import re
import urllib2
import csv
from urllib2 import urlopen
import pandas as pd

# from urllib.request import urlopen
from bs4 import BeautifulSoup

contents = []

f = csv.writer(open('GLO.csv', 'w'))
# f.writerow(['Title','Date','Publisher','Description','Download'])

with open('plssLinks.csv','r') as csvf: # Open file in read mode
    urls = csv.reader(csvf)
    for url in urls:
        contents.append(url) # Add each url to list contents

for url in contents:  # Parse through each url in the list.
	page = urlopen(url[0]).read()
	soup = BeautifulSoup(page, "html.parser")
	table = soup.find('table')
	table_rows = table.find_all('tr')

	for tr in table_rows:
		td = tr.find_all('td')
		row = [tr.text for tr in td]
		print(row)















