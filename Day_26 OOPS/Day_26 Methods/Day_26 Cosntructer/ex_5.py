# parameterless Constructer

class SpecialMethod:
    def __init__(self):
        self.methodname = "__init__ is a Constructer"
        self.name_2 = "reserved method"
    def details(self):
        print(self.name_2)
        print(self.methodname)

obj = SpecialMethod()
obj.details()
