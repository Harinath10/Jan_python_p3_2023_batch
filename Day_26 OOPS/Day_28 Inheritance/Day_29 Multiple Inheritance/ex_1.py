class A:
    def add_a(self):
        print(100+500)

class B:
    def sub_b(self):
        print(100-23)

class C:
    def mul_c(self):
        print(10*" python ")

class D(A,B,C):
    def div_d(self):
        print(4/3)


class E(B,C):
    def d_d(self):
        print(9/3)

obj_d = D()

obj_d.add_a()
obj_d.sub_b()
obj_d.mul_c()
obj_d.div_d()

print("-----------------")
e=E()
e.d_d()
e.mul_c()
e.sub_b()