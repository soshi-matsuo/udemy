import mysql.connector

conn = mysql.connector.connect(host='localhost', user='root', password='root', database='test_db')
cur = conn.cursor()

# cur.execute('create table persons('
#             'id int NOT NULL AUTO_INCREMENT,'
#             'name varchar(14) NOT NULL,'
#             'PRIMARY KEY(id))')

cur.execute('insert into persons(name) values("Mike")')
conn.commit()

cur.execute('select * from persons')
for row in cur:
    print(row)
cur.close()
conn.close()