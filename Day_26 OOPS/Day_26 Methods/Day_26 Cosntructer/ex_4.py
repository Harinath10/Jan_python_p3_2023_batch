# parameterless Constructer

class SpecialMethod:
    def __init__(self):
        self.methodname = "__init__ is a Constructer"
        self.name_2 = "reserved method"
        print(self.methodname)
        print(self.name_2)

obj = SpecialMethod()
