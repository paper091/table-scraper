import requests
from bs4 import BeautifulSoup

url = 'https://www.skysports.com/premier-league-table'

rawData = requests.get(url)
soup = BeautifulSoup(rawData.text, 'html.parser')

league_table = soup.find("table", class_ = "standing-table__table callfn")
print(league_table)