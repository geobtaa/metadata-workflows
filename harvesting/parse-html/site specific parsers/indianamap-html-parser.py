import csv
import re
import urllib2

from urllib2 import urlopen

from bs4 import BeautifulSoup

portalMetadata = []

f = csv.writer(open('results.csv', 'w'))
f.writerow(['Title','Description','Tags','Creator','Links'])

with open('indianamap.csv','r') as harvest:
    urls = csv.reader(harvest)
    for url in urls:
        portalMetadata.append(url)

for url in portalMetadata:
	page = urlopen(url[0]).read()
	soup = BeautifulSoup(page, "html.parser")

	titleField = soup.find(attrs={'id': 'subheader'})
	descriptionField = soup.find(attrs={'id': 'Comments'})
	creatorField = soup.find(attrs={'id': 'Credits'})
	tagField = soup.find(attrs={'id': 'Tags'})
	serviceField = soup.find(attrs={'id': 'Tags'})
	links = []

	for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
		links.append(link.get('href'))

# 	metadataLink = soup.find('a', href=True, id='fgdc')
# 	downloadLink = soup.find('a', href=True, text='fgdc')


	title = titleField.text.strip(),
	description = descriptionField.text.strip(),
	creator = creatorField.text.strip(),
	tags = tagField.text.strip(),
	linksies = links

# 	metadata = metadataLink['href'],


	f.writerow([title,description,creator,tags,linksies])
















