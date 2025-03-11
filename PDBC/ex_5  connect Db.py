import credentials
import mysql.connector

hostname = credentials.hostname
user = credentials.username
password = credentials.password
db = credentials.sb_name

connection_db = mysql.connector.connect(host=hostname,user = user, password= password,database=db)
cur = connection_db.cursor()
cur.execute("show tables")

for each_table in cur:
    print(each_table)
