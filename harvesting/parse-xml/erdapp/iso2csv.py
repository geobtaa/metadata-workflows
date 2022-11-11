import csv
import re
import urllib.request
from urllib.request import urlopen
import csv
from bs4 import BeautifulSoup
import lxml

portalMetadata = []

f = csv.writer(open('erdapp-output.csv', 'w'))
f.writerow(['Identifier','Title','Description','Originator','Date_Issued','Topic','West','East','North','South','Format','links','keywords'])

with open('inputxmls.csv','r') as harvest:
    urls = csv.reader(harvest)
    for url in urls:
        portalMetadata.append(url)

for url in portalMetadata:
	page = urlopen(url[0]).read()
	soup = BeautifulSoup(page, "xml")


	idField = soup.find('fileIdentifier')
	titleField = soup.find('title')
	abstractField = soup.find('abstract')
	originField = soup.find('credit')
	pubdateField = soup.find('date')
	topicField = soup.find('MD_TopicCategoryCode')
	westField = soup.find('westBoundLongitude')
	eastField = soup.find('eastBoundLongitude')
	northField = soup.find('northBoundLatitude')
	southField = soup.find('southBoundLatitude')
	formatField = soup.find('MD_Format')
	links = []
	for word in soup.select('URL'):
		links.append(word.contents[0])

	keywords = soup.find_all('keyword')
# 	keywords = []
# 	for word in soup.select("keyword")[0].get_text():
# 		keywords.append(word.contents[0])

	try:
		scraped_id = idField.text.strip()
	except:
		scraped_id = "undefined"
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
		scraped_topic = topicField.text.encode('utf-8').strip()
	except:
		scraped_topic = "undefined"

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
		scraped_link = links
	except:
		scraped_link = "undefined"
	try:
		scraped_keywords = keywords
	except:
		scraped_keywords = "undefined"


	f.writerow([scraped_id,scraped_title,scraped_abstract,scraped_origin,scraped_pubdate,scraped_topic,scraped_west,scraped_east,scraped_north,scraped_south,scraped_format,scraped_link,scraped_keywords])
















