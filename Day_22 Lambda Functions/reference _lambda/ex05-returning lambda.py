# RETURNING a LAMBDA

def arshad(a):
    return lambda b:b**a
x=arshad(4)       # a value
print(x(3))       # b value                 --> b power of a ==>81




def x(a):
    return lambda cc:cc+a
hy=x(6767)
print(hy(3))



def d1(a,b):
    return lambda c:c*a-b
xy=d1(6,4)
print(xy(10))
