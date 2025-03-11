class Country:
    def name_1(self):
        self.country_name = input("enter Country name:")
        print(self.country_name)
#
C = Country()
C.name_1()

class State(Country):
    def statename(self):
        self.name = input("enter State name:")
        print(self.name)
S = State()
S.statename()
S.name_1()

#
# class A:
#     def hello(self):
#         self.name = "aaa"
#         print(self.name)
#
# class B(A):
#     def name_2(self):
#         self.x = 12
#         print(self.x)
#
# obj  = B()
# obj.hello()
# obj.name_2()