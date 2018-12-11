import sqlite3

conn = sqlite3.connect(':memory:')

cur = conn.cursor()

cur.execute(
    'CREATE TABLE persons(ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME STRING)')
conn.commit()

cur.execute(
    'INSERT INTO persons(name) values(\'Mike\')'
)
cur.execute(
    'INSERT INTO persons(name) values(\'Takashi\')'
)
cur.execute(
    'INSERT INTO persons(name) values(\'Jun\')'
)
cur.execute(
    'INSERT INTO persons(name) values(\'Nancy\')'
)
conn.commit()

cur.execute(
    'UPDATE persons set name = "Michel" WHERE name = "Mike"'
)
conn.commit()
cur.execute(
    'SELECT * from persons'
)
print(cur.fetchall())

cur.close()

conn.close()