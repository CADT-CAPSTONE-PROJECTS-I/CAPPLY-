import requests
from bs4 import BeautifulSoup 
import sqlite3

conn = sqlite3.connect('src/db.sqlite3')
c = conn.cursor()

for i in range (1, 4):
    web_link = f'https://www.scholars4dev.com/page/{i}/'
    r = requests.get(web_link)
    soup = BeautifulSoup(r.content, 'lxml')

    lists = soup.find_all('div', id = 'contentleft')
    for list in lists:
        listing = list.find_all('div', class_ = 'entry clearfix')
        for info in listing:
            more_info = info.find('h2').a['href']
            school = info.find('h2').text
            country = info.find(string=lambda text: 'study' in text.lower())
            if country:
                country = country.text
            level = info.find(string=lambda text: 'degree' in text.lower())
            if level:
                level = level.text
            deadline = info.find(string=lambda text: '2023' in text.lower())
            if deadline:
                deadline = deadline.text

            c.execute('''INSERT INTO category_scholarship VALUES(?,?,?,?,?,?,?)''',(None, level, school, deadline, more_info, web_link, country))
            
conn.commit()
print('complete.')

#close connection
conn.close()

            