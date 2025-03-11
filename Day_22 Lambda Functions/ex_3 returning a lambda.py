# returning a lambda

def data(a):
    return lambda b :a**b

y = data(2)
print(y(3))