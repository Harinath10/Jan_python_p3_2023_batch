class Python:        # Classname is Python
    a= 1                # class V
    b = 5               # class V

    def setHello(self):        # it is a instance method ( methodname hello())
        self.course = "Python"    # instance V
        self.Duration= "3 mon"    # instance V

    def getHello(mouse):
        print(mouse.course)
        print(mouse.Duration)
        # print(a)   # NameError: name 'a' is not defined
        print(mouse.a)  # calling class variable with the help of Mouse
        print(mouse.b)  # calling class variable with the help of mouse
        print("\n")
        print(Python.a)   # calling class variable with the help of class name
        print(Python.b)   # calling class variable with the help of class name

obj = Python()      #  Python is a Object ( Obj is a Object)
obj.setHello()
obj.getHello()
print(obj.a)
print(obj.b + obj.a)
print("\n")

print(Python.a-Python.b)