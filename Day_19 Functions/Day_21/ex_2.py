# global variable accessing inner function

course = "Python Backend"

def f1():
    print("this is ",course)
    def f2():
        print("this is iNner fumction")
        print(course)
    f2()
f1()
