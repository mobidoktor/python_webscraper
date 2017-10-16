import requests
from BeautifulSoup import BeautifulSoup

url = 'https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s'
response = requests.get(url)
html = response.content
# <tbody class="stripe" id="mrc_main_table">

soup = BeautifulSoup(html)
table = soup.find('tbody', attrs={'class': 'stripe'})
print table.prettify()