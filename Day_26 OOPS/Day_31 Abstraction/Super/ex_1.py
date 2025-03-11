class A:
    def res(self):
        print("this is from A ")

class B(A):
    def res(self):
        super().res()
        print("this is from B")



class C(B):
    def res(self):
        print("this is from Child C")
        super().res()

obj = C()
obj.res()

