import sqlite3
conn = sqlite3.connect('demo_data.sqlite3')
import os
os.listdir()
query = 'CREATE TABLE demo (s TEXT, x INT, y INT);'
query
curs = conn.cursor()
curs.execute(query)
curs.close()
conn.commit()
curs2 = conn.cursor()
curs2.execute('SELECT * FROM demo;').fetchall()
insert_query1 = "INSERT INTO demo (s, x, y) VALUES ('g', 3, 9);"
insert_query2 = "INSERT INTO demo (s, x, y) VALUES ('v', 5, 7);"
insert_query3 = "INSERT INTO demo (s, x, y) VALUES ('f', 8, 7);"
curs2.execute(insert_query1)
curs2.execute(insert_query2)
curs2.execute(insert_query3 )
curs2.close()
conn.commit()
curs3 = conn.cursor()
query = ''' SELECT COUNT(*) FROM demo;'''

curs3.execute(query).fetchall()

query = ''' SELECT COUNT(*) FROM demo WHERE x>5 AND y>5;'''

curs3.execute(query).fetchall()

query = '''SELECT COUNT (DISTINCT y) FROM demo;

curs3.execute(query).fetchall()