# class A:
#
#     def data(self):
#         self.firstname = "python"
#         self.secondname = "AWS"
#
#         print(self.firstname,self.secondname)
#
# class B(A):
#     def get_value(self):
#         print(self.firstname,self.secondname,"<== accessing from parent Class")
#
# obj = B()
# obj.data()
# obj.get_value()


print("-----------------------------------------------------------------")


class A:

    def data(self):
        self.__firstname = "python"
        self.secondname = "AWS"

        print(self.__firstname,self.secondname)
    def get_data(self):
        print(self.__firstname)

class B(A):
    def get_value(self):
        print(self.__firstname,"<== accessing from parent Class")

obj = B()
obj.data()
obj.get_value()
