import mysql.connector
# print(dir(mysql.connector))

# con = mysql.connector.connect(host="localhost",user = "root",password ="root")
# print("Connection Sucessful")

###    Or

# con = mysql.connector.connect(host="127.0.0.1",user = "root",password ="root")
# print("Connection Sucessful")

###    Or

hostname = "127.0.0.1"
username = "root"
password = "root"

con = mysql.connector.connect(host=hostname,user = username,password =password)

print("connection Success")
