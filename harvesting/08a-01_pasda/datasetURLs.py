import csv
import time
import urllib.request
from bs4 import BeautifulSoup

# the keyword value(+) referring to the input whitespace in search box might return all dataset?
resURL = 'https://www.pasda.psu.edu/uci/SearchResults.aspx?Keyword=+'
page = urllib.request.urlopen(resURL).read()
soup = BeautifulSoup(page, 'html.parser')

# table contains all dataset links that start with 'a' html tag
table = soup.find('table', id="DataGrid1")    
hrefs = table.findAll('a')

urls = []
for href in hrefs:
    url = 'https://www.pasda.psu.edu/uci/' + href['href']
    urls.append([url])


# write all dataset urls in csv file with actiondate
actionDate = time.strftime('%Y%m%d')
with open(f'pasdaURLS_{actionDate}.csv', 'w') as fw:
    writer = csv.writer(fw)
    writer.writerows(urls)

