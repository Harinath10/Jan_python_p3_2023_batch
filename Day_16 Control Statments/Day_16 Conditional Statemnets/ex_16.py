name = ["Naveen","ROSHINI","Amar"]
password= ["12345","abcde","a123","hello"]

user_name = input("enter User NAme: ")

if name[0] == user_name:

    print("\n hello",name[0])

    user_password = input("enter password: ")

    if password[0] == user_password:
        print("Matched Details .\n Welcome",name[0])
    elif password[1] == user_password:
        print("second password matched")
    else:
        print("paswd notmatched")

elif name[1] == user_name:
    print("\n Hai",name[1])

elif name[2] == user_name:
    print("\n____hello____",name[2])

else:
    print("\n no matches Found")