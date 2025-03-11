class A:
    def data(self):
        print("hello")

class B:
    def data(self):
        print("Python")
#
# first_obj = A()
# first_obj.data()
# second_obj = B()
# second_obj.data()

for obj in A(),B():
    obj.data()            # Duck TYping