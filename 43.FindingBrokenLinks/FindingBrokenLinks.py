import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup

url = 'https://covid-19-dc.herokuapp.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

links = soup.find_all('a')
print('Total links are', len(links))

for link in links:
    url = link.get('href')
    if url is not None and urlparse(url).scheme in ('http', 'https'):
        try:
            response = requests.head(url)
            if response.status_code == 200:
                print(url, '- OK')
            else:
                print(url, '- ' + str(response.status_code))
        except requests.exceptions.RequestException:
            print(url, '- Failed to connect')
