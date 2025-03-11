# way _2

class Class_method_related:
    first_class_V = "class A"
    second_class_V = "class B"

    def details(cls):
        first = 100
        second = 200
        print(first)
        print(second)
        print("\n")
        print(Class_method_related.first_class_V)
        print(Class_method_related.second_class_V)
Class_method_related.details =classmethod(Class_method_related.details)
Class_method_related.details()