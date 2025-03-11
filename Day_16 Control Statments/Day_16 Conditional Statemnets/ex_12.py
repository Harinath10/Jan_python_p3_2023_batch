# data = "hello world"
# print(list(data))
list_val = ['h', 'e', 'l', 'l', 'o', '13', 'w', 'o', 'r', 'l', 'd']
check = input("enter charecter: ")

if check in list_val and len(list_val) >= 5:
    print(check, " is available")

elif list_val[5].isdigit() and list_val.count("l") > 11:
    print("first elif block executed")

elif list_val[5].isdigit() and list_val.count("l") > 1:
    print("second elif block executed")

    name = "harinath"
    check_option = input("enter your name:")
    if name.casefold() == check_option.casefold():
        print("login Success")
        print("thanks for Visiting")

    else:
        print("Login failed")
        print("try again")

else:
    print(check, " is not available ")
