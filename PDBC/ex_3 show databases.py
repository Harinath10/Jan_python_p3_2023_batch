import mysql.connector

hostname = "localhost"
user = "root"
password ="root"

mydb = mysql.connector.connect(user = user,password =password,host=hostname)
print("connection Success")
mycur = mydb.cursor()
mycur.execute("show databases")

for each_db in mycur:
    print(each_db)