#way one

class Static_Class:
    first_class_V = "class A"
    second_class_V = "class B"

    @staticmethod
    def details():
        first = 100
        second = 200
        print(first)
        print(second)
        print("\n")
        print(Static_Class.first_class_V)
        print(Static_Class.second_class_V)

S= Static_Class
S.details()


print("\n -----------------")

S2 = Static_Class()
S2.details()

