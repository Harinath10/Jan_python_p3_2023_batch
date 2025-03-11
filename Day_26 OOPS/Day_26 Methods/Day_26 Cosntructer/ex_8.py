# parameterless Constructer

class SpecialMethod:

    def __init__(sql):
        sql.methodname = "__init__ is a Constructer"
        sql.name_2 = "reserved method"
    def details(self):
        print(self.name_2)
        print(self.methodname)


obj = SpecialMethod()
obj.details()
