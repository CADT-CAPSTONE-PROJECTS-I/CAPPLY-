import requests
from bs4 import BeautifulSoup 
import sqlite3
conn = sqlite3.connect('src/db.sqlite3')
c = conn.cursor()

for i in range (1, 41):
    web_link = f'https://www.idp.com/cambodia/search/scholarship/?studyLevel=%3Aundergraduate&page={i}'
    r = requests.get(web_link)
    soup = BeautifulSoup(r.content, 'lxml')
    lists = soup.find_all('div', class_ = 'pro_wrap')
    for list in lists:
        listing = list.find_all('div', class_ = 'pro_list_wrap')
        for info in listing: 
            link = info.find('a', class_ = 'prdct_lnk').get('href')
            more_info = 'https://www.idp.com' + link
            schools = info.find('div', class_ = 'ins_cnt')
            school = schools.a.text.strip() 
            country = schools.p.text.strip().split(',')[-1].strip()
            level = info.find('div', class_ = 'media_txt').text.strip().split('Qualification')[-1].strip()
            deadline = 'more'
            c.execute('''INSERT INTO category_scholarship VALUES(?,?,?,?,?,?,?)''',(None, level, school, deadline, more_info, web_link, country))
conn.commit()
print('complete.')

#close connection
conn.close()