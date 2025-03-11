import credentials
import mysql.connector

hostname = credentials.hostname
user = credentials.username
password = credentials.password
db = credentials.sb_name

connection_db = mysql.connector.connect(host=hostname,user = user, password= password,database=db)
cur = connection_db.cursor()
query= "insert into details(name) values (%s)"
val = [("Riyaz")]
cur.execute(query,val)
connection_db.commit()

print(cur.rowcount,"was inserted")
