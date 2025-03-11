# parameterless Constructer

class SpecialMethod:

    def __init__(xyz):
        xyz.methodname = "__init__ is a Constructer"
        xyz.name_2 = "reserved method"
        print(xyz.name_2)
        print(xyz.methodname)


obj = SpecialMethod()

