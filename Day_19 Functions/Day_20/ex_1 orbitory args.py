# orbitory arguments


def data(*roll):

    print(roll)
    print(type(roll))

    print(roll[5])
    print(roll[-5])
    print(roll[5:])
data(1,"10",21,True,False,5+8j,100.0)