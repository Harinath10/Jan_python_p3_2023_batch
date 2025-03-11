# parameterless Constructer

class SpecialMethod:
    name = "python"      # class Variable
    print(name,"<--- accesing Direct approach")
    def __init__(xyz):
        xyz.methodname = "__init__ is a Constructer"
        xyz.name_2 = "reserved method"
        # print(name)
        print(SpecialMethod.name,"<-- accessing using class name ")  # class variables we can access using class name


obj = SpecialMethod()

