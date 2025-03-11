username =["Tharun","lokesh","Pavan","lakshmi"]
password =["Tharun","lokesh","Pavan","lakshmi"]

name = input("enter user name: ")
pswd= input("enter your password: ")

if username.index(name) == (password.index(pswd)):
    print("login succcess")
else:
    print("login failed")
