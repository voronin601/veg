import requests
import psycopg2 as pg2
import re
import unicodedata

a = requests.get('https://www.google.com/maps/d/u/0/embed?mid=1cqWbHiCxxj3mPgYsbphYLAjmyhg&ll=59.9242102963437%2C30.359042849576554&z=15')

conn = pg2.connect(dbname = 'postgres', user = 'postgres', password = 'vovavoronin@1999', host = '127.0.0.1', port = '5432')
cursor = conn.cursor()

html = a.text

rest = html.split('Название:')[1:-1]

'''with open('E:\syit\qwe.txt','w', encoding='utf-8') as t:
    for idd, i in enumerate(rest):
        t.write(str(idd) + i + '\n\n')'''

for idd, i in enumerate(rest):
    b = []
    q = i.split('Сведения из Google Карт')[0].split('\\",[\\"')[1].split('\\"]\\n,1]')[0].replace(u'\xa0', u' ')
    if q[-2:] == "\n": b.append(q.split('\\')[0])
    else: b.append(q)
    try:
        b.append(i.split('Сведения из Google Карт')[0].split('[[\\"Адрес:\\",[\\"')[1].split('\\"]\\n,1]')[0].replace(u'\xa0', u' '))
    except:
        if len(b) == 2: pass
        else:b.append('-')
    try:
        q = i.split('Сведения из Google Карт')[0].split('[\\"Сайт:\\",[\\"')[1].split('\\"]\\n')[0].replace(u'\xa0', u' ')
        if q[-2:] == "\n": b.append(q.split('\\')[0])
        else: b.append(q)
    except:
        if len(b) == 3: pass
        else:b.append('-')
    try:
        q = i.split('Сведения из Google Карт')[0].split('[\\"Телефон:\\",[\\"')[1].split('\\"]')[0].replace(u'\xa0', u' ')
        if q[-2:] == "\n": b.append(q.split('\\')[0])
        else: b.append(q)
    except:
        if len(b) == 4: pass
        else:b.append('-')
    
    cursor.execute("INSERT INTO rest VALUES ('%s', '%s', '%s', '%s');" %(b[0], b[1], b[2], b[3]))
    conn.commit()
    
    print(idd, end = "\r")