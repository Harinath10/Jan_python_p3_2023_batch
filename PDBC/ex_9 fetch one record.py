import credentials
import mysql.connector

hostname = credentials.hostname
user = credentials.username
password = credentials.password
db = credentials.sb_name

connection_db = mysql.connector.connect(host=hostname,user = user, password= password,database=db)
cur = connection_db.cursor()
cur.execute("select fname from emp")


#
# for each in cur.fetchone():
#     print(each)



for each in cur.fetchall():
    print(each)