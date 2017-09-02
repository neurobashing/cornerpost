#!/usr/bin/env python3

import sqlite3
conn = sqlite3.connect('food.db')
c = conn.cursor()
c.execute('drop table meals')
conn.commit()
c.execute('CREATE TABLE meals (name text, protein text, season text)')
conn.commit()
with open('source.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]
for item in content:
    c.execute("INSERT INTO meals (name) VALUES ('" + item + "')")
conn.commit()    
conn.close()