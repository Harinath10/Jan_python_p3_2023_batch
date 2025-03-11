# parameterless Constructer

class SpecialMethod:
    methodname = "abcdefgh"   # classV
    def __init__(self):
        self.methodname = "__init__ is a Constructer"   # constructer V
        self.name_2 = "reserved method"                 # constructer V
        print(self.methodname)
        print(self.name_2)
        print(SpecialMethod.methodname)

obj = SpecialMethod()
