

def f1(a,b):


    if a is b:
        print("a and b values and memory location same")
    elif a == b:
        print("a and b values Matched")
    else:
        print("no values matched")

f1(10,10.0)
print("\n")
f1(100,100)
print("\n")
f1(50,500)

