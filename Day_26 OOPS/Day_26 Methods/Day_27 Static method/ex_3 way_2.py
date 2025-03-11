# way _2

class Static_Class:
    first_class_V = "class A"
    second_class_V = "class B"

    def details():
        first = 100
        second = 200
        print(first)
        print(second)
        print("\n")
        print(Static_Class.first_class_V)
        print(Static_Class.second_class_V)
Static_Class.details =staticmethod(Static_Class.details)
Static_Class.details()