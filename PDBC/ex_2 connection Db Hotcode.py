import mysql.connector
import credentials
hostname = credentials.hostname
username = credentials.username
password = credentials.password

con = mysql.connector.connect(host=hostname,user = username,password =password)

print("connection Success")