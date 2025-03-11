# way_1

class Class_mehod:

    @classmethod
    def details(cls):
        cls.name = "Manu"
        cls.des = "ASE"
        print(cls.name,cls.des)

C = Class_mehod
C.details()

print("\n")
Class_mehod().details()