name = "Pavan"

def d1():
    name = "Ramesh"
    print(name, " is Local Variable")
    print(globals()["name"] ,"is global variable")
d1()