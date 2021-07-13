"""
Created on Tue Jul 13 04:38:01 2021

@author: Tyrone Shaffer
"""
import requests
from bs4 import BeautifulSoup

combo_URLs = 'http://www.dustloop.com/wiki/index.php?title=GGST/Ky_Kiske/Combos'

page = requests.get(combo_URLs)

soup = BeautifulSoup(page.content, 'html.parser')

combo_tables = soup.find_all('table', class_='wikitable sortable')
print(combo_tables)

for table in combo_tables:
    rows = table.findChildren('tr')
    
    for row in rows:
        cells = row.findChildren('td')
        for c in range(len(cells)):
            if(c == 0):
                print('Moves: ')
                moves = cells[c].find_all('span')
                for move in moves:
                    print(move.text.strip())