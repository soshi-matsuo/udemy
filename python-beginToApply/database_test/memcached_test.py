import sqlite3
import memcache
import time


db = memcache.Client(['127.0.0.1:11211'])

# db.set('teset', 'valueee', time=5)
# time.sleep(7)
# print(db.get('teset'))

conn = sqlite3.connect('test_sqlitemem.db')
cur = conn.cursor()

# cur.execute(
#     'create table persons('
#     'employ_id integer primary key autoincrement, name string)')

# cur.execute('insert into persons(name) values("Mike")')
# # conn.commit()

# cur.close()
# conn.close()

def get_employ_id(name):
    # query to memcache
    employ_id = db.get(name)
    if employ_id:
        return employ_id
    # query to sqlite
    cur.execute(
        'select * from persons where name = "{}"'.format(name)
    )
    person = cur.fetchone()
    if not person:
        raise Exception('No employ')
    employ_id, name = person
    db.set(name, employ_id, time=60)
    return employ_id

print(get_employ_id('Mike'))