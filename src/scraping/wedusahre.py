import requests
from bs4 import BeautifulSoup 
import sqlite3

conn = sqlite3.connect('src/db.sqlite3')
c = conn.cursor()

for i in range(1, 17):
    link_web = f'https://www.wedushare.com/all-program/Master?page={i}'
    r = requests.get(link_web)
    soup = BeautifulSoup(r.content, 'lxml')
    lists = soup.find_all('div', class_ = 'article-list grid-2 mb-2')
    for list in lists:
        listing = list.find_all('div', class_ = 'item shadow--hover')
        for link in listing:
            school = link.find('a', class_ = 'text-default text-sub sub-2').text
            more_info = link.find('a', class_ = 'text-default text-sub sub-2').get('href')
            deadline = link.find('span').text
            countries = link.find('div', class_ = 'col')
            country = countries.span.text
            level = link.find_all('span', class_ = 'text-muted text-sm')[1].text
            study_field = 'option'
            c.execute('''INSERT INTO category_scholarship VALUES(?,?,?,?,?,?,?)''',(None, level, school, deadline, more_info, link_web, country))
            
conn.commit()
print('complete.')

#close connection
conn.close()