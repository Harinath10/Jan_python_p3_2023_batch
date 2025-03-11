

def f1(a,b):


    if a is b:
        print("a and b values and memory location same")
    elif a == b:
        print("a and b values Matched")
    else:
        print("no values matched")


def data(name,age):   # name , age --> parameters
    print(name)
    print(age)
    f1(10,20)



def details():
    x = 100
    y = 200

    if y>x:
        f1(50,50)
    elif x>y:
        data("java",15)
    else:
        pass
details()