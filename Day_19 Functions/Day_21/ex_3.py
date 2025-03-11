# global variable accessing inner function



def f1():
    print("this is ",course)
    def f2():
        course = "Python Backend"
        print("this is iNner fumction")
        print(course)
    f2()
f1()
