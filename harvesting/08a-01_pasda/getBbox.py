import csv
import re
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

portalMetadata = []

f = csv.writer(open('bbox-output-test.csv', 'w'))
f.writerow(['url','bbox'])

with open('sample-inputMetadataUrls.csv','r') as harvest:
     urls = csv.reader(harvest)
     for url in urls:
        portalMetadata.append(url)

for url in portalMetadata:
      try:
            page = urlopen(url[0]).read()
            soup = BeautifulSoup(page, "html.parser")
            pageLink =str(url)[1:-1].strip("\'")
      
            try:
                  west = soup.find('i',string='West_Bounding_Coordinate:').next_sibling.strip()   
            except:
                  west = ''
            
            try:
                  south = soup.find('i',string='South_Bounding_Coordinate:').next_sibling.strip()   
            except:
                  south = ''
            
            try:
                  east = soup.find('i',string='East_Bounding_Coordinate:').next_sibling.strip()   
            except:
                  east = ''
            
            try:
                  north = soup.find('i',string='North_Bounding_Coordinate:').next_sibling.strip()   
            except:
                  north = ''
            
            bbox = west + ',' + south + ',' +east+','+north
      except:
            bbox = "would not open"
       
      f.writerow([pageLink,bbox])
      



















