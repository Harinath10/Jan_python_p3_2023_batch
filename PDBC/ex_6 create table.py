import credentials
import mysql.connector

hostname = credentials.hostname
user = credentials.username
password = credentials.password
db = credentials.sb_name

connection_db = mysql.connector.connect(host=hostname,user = user, password= password,database=db)
cur = connection_db.cursor()
cur.execute("create table emp(fname varchar(100),lname varchar(100))")

print("table created")

for each in cur:
    print(each)