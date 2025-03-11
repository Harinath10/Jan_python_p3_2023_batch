import credentials
import mysql.connector

hostname = credentials.hostname
user = credentials.username
password = credentials.password

connection_db = mysql.connector.connect(host=hostname,user = user, password= password)
cur = connection_db.cursor()
# cur.execute("create database riyaz")
print("db is Created")
cur.execute("show databases")

for each in cur:
    print(each)