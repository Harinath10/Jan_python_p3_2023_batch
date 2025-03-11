
# Orbitory keyword argumenst

def bikes( **details ):
    print(details)
    print(details["b_name"])
    print(details["milage"])
    print(details["price"])
    # print("Owner is :",details["owner"])
    print("\n")

bikes(b_name = "R15",price = 215000,milage = 35,owner ="A")
bikes(b_name = "mt15",price = 258000,milage = 30)
bikes(b_name = "KTM",price = 200000,milage = 35)
bikes(b_name = "royal enfield",price = 215000,milage = 45, owner = "abcd")