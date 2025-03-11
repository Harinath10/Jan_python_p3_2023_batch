#way one

class Static_Class:
    first_class_V = "class A"
    second_class_V = "class B"

    @staticmethod
    def details(first,second):

        print(first)
        print(second)
        print(first + second)
        print("\n")
        print(Static_Class.first_class_V)
        print(Static_Class.second_class_V)

S= Static_Class
S.details(10,20)


print("\n -----------------")

S2 = Static_Class()
S2.details("hello","python")

