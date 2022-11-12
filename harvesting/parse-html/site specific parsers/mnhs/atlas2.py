import csv
import re
import urllib2

from urllib2 import urlopen

from bs4 import BeautifulSoup

portalMetadata = []

f = csv.writer(open('atlasReport.csv', 'w'))
f.writerow(['Title'])

with open('atlas3.csv','r') as harvest:
    urls = csv.reader(harvest)
    for url in urls:
        portalMetadata.append(url)

for url in portalMetadata:
	page = urlopen(url[0]).read()
	soup = BeautifulSoup(page, "html.parser")

	titleField = soup.find(attrs={'class': 'description'})
	# titleField = []
#
# 	for word in soup.find_all('Titles'):
# 		titleField.append(word.contents[0])


	f.writerow([titleField])
















