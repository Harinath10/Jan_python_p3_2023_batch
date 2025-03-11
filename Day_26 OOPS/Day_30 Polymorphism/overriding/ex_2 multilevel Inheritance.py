class A:
    def data(self):
        self.val = 100
        print(self.val)

    def name_data(self):
        self.name = "Python"
        print(self.name)
    def modules(self):
        self.module_math = "math"
        self.module_random = "random"
        self.module_pandas = "pandas"
    def get_modules(self):
        print(self.module_math)
        print(self.module_random)
        print(self.module_pandas)

class B(A):
    def set_name(self):
        self.name = "hello "
        self.homepage = "Wel come to Home page"
    def get_name(self):
        print(self.name)
        print(self.homepage)

    def modules(self):
        self.module_os = "OS"
        self.module_time = "time"
        self.module_date = "date"
        self.module_calender = "calender"

    def get_modules(self):
        print(self.module_os , self.module_time)
        print(self.module_date, self.module_calender)
        # print(self.module_random,"Accessing from class A")

class C(B):
    def modules(self):
        self.numpies = "Numpy"
        self.tkinter = "tkinter"
    def get_modules(self):
        print(self.numpies)
        print(self.tkinter)


obj = C()
obj.data()
obj.name_data()
obj.set_name()
obj.get_name()
obj.modules()
obj.get_modules()

print("\n --------------> class A")
obj_a = A()
obj_a.modules()
obj_a.get_modules()

print("\n --------------> class B")

obj_b = B()
obj_b.modules()
obj_b.get_modules()

print("\n --------------> class C")
obj_c = C()
obj_c.modules()
obj_c.get_modules()
