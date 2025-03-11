name = {"firstname":input("enter your name:"),"second name":input("enter your lastname:"),"pin":eval(input("enter your pin number:"))}
print(name)
print(type(name["pin"]))

val = name["pin"]
converting_to_int = int(val)
print(converting_to_int)
print(type(converting_to_int))