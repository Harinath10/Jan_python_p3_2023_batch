class A:

    def __init__(self):
        print("This is Constructer or Special Method , It can call Automatically")

    def set_user_details(self):
        print("this is first Instance Method , and it is Coming from Class A")

    def admin_details(self):
        print("this is Second Instance Method , and it is Coming from Class A")
        print("this is for Admin _details")


a = A()
a.set_user_details()
a.admin_details()


class B(A):

    def instance_check(self):
        print("\n", "this is first Instance Method , and it is Coming from Class B")

    def part_2(self):
        print("\n", "this is Second Instance Method , and it is Coming from Class B")
        print("\n", "this is for PArt_2")


b = B()
b.instance_check()
b.part_2()
print("---------single Relation--------accessing parent class propertise-----------")
b.set_user_details()
b.admin_details()
print("-------------accessing child class propertise----------------")
b.instance_check()
b.part_2()
