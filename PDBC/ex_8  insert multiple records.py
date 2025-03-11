import credentials
import mysql.connector

hostname = credentials.hostname
user = credentials.username
password = credentials.password
db = credentials.sb_name

connection_db = mysql.connector.connect(host=hostname,user = user, password= password,database=db)
cur = connection_db.cursor()
query= "insert into emp(fname,lname) values (%s,%s)"
val = [
    ('Peter', 'Lowstreet 4'),
    ('Amy', 'Apple st 652'),
    ('Hannah', 'Mountain 21'),
    ('Michael', 'Valley 345'),
    ('Sandy', 'Ocean blvd 2'),
    ('Betty', 'Green Grass 1'),
    ('Richard', 'Sky st 331'),
    ('Susan', 'One way 98'),
    ('Vicky', 'Yellow Garden 2'),
    ('Ben', 'Park Lane 38'),
    ('William', 'Central st 954'),
    ('Chuck', 'Main Road 989'),
    ('Viola', 'Sideway 1633')
]
cur.executemany(query, val)
connection_db.commit()

print(cur.rowcount,"was inserted")
