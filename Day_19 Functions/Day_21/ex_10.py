def d1():
    X=10
    print("d1 scope:",X)
    def d2():
        y=20
        X = 40
        print('D2 SCOPE:',X)
        print('D1 SCOPE:',y)
    return d2
res = d1()
res()
