# function Returning
def d1(a,b):
    def d2():
        return a+b
    return d2()
x=d1(10,5)
print(x)
