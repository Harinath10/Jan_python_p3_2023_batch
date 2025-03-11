

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

data("Python",11)    # python , 11 --> arguments
