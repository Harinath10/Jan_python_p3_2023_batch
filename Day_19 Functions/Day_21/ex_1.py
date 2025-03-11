# function inside another function

def d1():
    print("This is Outer Function")
    def d2():
        print("This is Inner Function")
    d2()

d1()
