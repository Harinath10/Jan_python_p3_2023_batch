# orbitory arguments


def data(*roll):
    x = "12345"
    print(x)
    print(roll)
    print(type(roll))

    if x.isdigit():
        print(x," X has numbers")
    else:
        print(x ," has no numbers")
    print(roll[5])
    print(roll[-5])
    print(roll[5:])
data(1,"10",21,True,False,5+8j,100.0)