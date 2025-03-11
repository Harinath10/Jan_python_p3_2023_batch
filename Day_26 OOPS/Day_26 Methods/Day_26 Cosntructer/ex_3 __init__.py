# parameterless Constructer

class SpecialMethod:
    def __init__(self):
        self.methodname = "__init__ is a Constructer"
        self.name_2 = "reserved method"

obj = SpecialMethod()
print(obj.methodname)
print(obj.name_2)

print("\n")
obj_2 = SpecialMethod()
print(obj_2.name_2)
print(obj_2.methodname)

