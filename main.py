import requests
from bs4 import BeautifulSoup as BS
from const import URL, USER_AGENT

response = requests.get(URL, headers=USER_AGENT)
soup = BS(response.text, 'lxml')
div = soup.find('div', id='block-nbl-content')
teams = div.find_all('span', class_='division-statistics-item__name')
result = []

for item in teams:
    result.append(item.text)





