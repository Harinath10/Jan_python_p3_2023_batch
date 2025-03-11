def func1():
    name = "hello"
    print(name)

def func_2():
    a= func1()
    print(a)
func_2()

print("\n")




def func1():
    name = "hello"
    print(name)
    return name

def func_2():
    a= func1()
    print(a)
func_2()