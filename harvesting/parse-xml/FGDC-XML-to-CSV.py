import csv
import re
import urllib2

from urllib2 import urlopen

from bs4 import BeautifulSoup

portalMetadata = []

f = csv.writer(open('05a-01_results.csv', 'w'))
f.writerow(['Title','Description','Originator','Date_Issued','Geom_type','West','East','North','South','Format','Thumbnail','Keywords'])

with open('05a-01.csv','r') as harvest:
    urls = csv.reader(harvest)
    for url in urls:
        portalMetadata.append(url)

for url in portalMetadata:
	page = urlopen(url[0]).read()
	soup = BeautifulSoup(page, "xml")


	titleField = soup.find('title')
	abstractField = soup.find('abstract')
	originField = soup.find('origin')
	pubdateField = soup.find('pubdate')
	geomField = soup.find('sdtstype')
	westField = soup.find('westbc')
	eastField = soup.find('eastbc')
	northField = soup.find('northbc')
	southField = soup.find('southbc')
	formatField = soup.find('native')
	thumbField = soup.find('browsen')
	keywords = []
	for word in soup.find_all('themekey'):
		keywords.append(word.contents[0])

	try:
		scraped_title = titleField.text.strip()
	except:
		scraped_title = "undefined"
	try:
		scraped_abstract = abstractField.text.encode('utf-8').strip()
	except:
		scraped_abstract = "undefined"
	try:
		scraped_origin = originField.text.encode('utf-8').strip()
	except:
		scraped_origin = "undefined"
	try:
		scraped_pubdate = pubdateField.text.encode('utf-8').strip()
	except:
		scraped_pubdate = "undefined"
	try:
		scraped_geom = geomField.text.encode('utf-8').strip()
	except:
		scraped_geom = "undefined"
	try:
		scraped_west = westField.text.strip()
	except:
		scraped_west = "undefined"
	try:
		scraped_east = eastField.text.strip()
	except:
		scraped_east = "undefined"
	try:
		scraped_north = northField.text.strip()
	except:
		scraped_north = "undefined"
	try:
		scraped_south = southField.text.strip()
	except:
		scraped_south = "undefined"
	try:
		scraped_format = formatField.text.strip()
	except:
		scraped_format = "undefined"
	try:
		scraped_keywords = keywords
	except:
		scraped_keywords = "undefined"
	try:
		scraped_thumb = thumbField.text.strip()
	except:
		scraped_thumb = "undefined"


	f.writerow([scraped_title,scraped_abstract,scraped_origin,scraped_pubdate,scraped_geom,scraped_west,scraped_east,scraped_north,scraped_south,scraped_format,scraped_thumb,scraped_keywords])
















