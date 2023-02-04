import requests
from bs4 import BeautifulSoup

url = 'https://www.skysports.com/premier-league-table'

rawData = requests.get(url)
soup = BeautifulSoup(rawData.text, 'html.parser')

league_table = soup.find('table', class_ = 'standing-table__table callfn')

for team in league_table.find_all('tbody'):
    rows = team.find_all('tr')
    for row in rows:
        row_data = row.find_all('td',  class_ = 'standing-table__cell')
        for data in row_data:
            print(data.text.strip())