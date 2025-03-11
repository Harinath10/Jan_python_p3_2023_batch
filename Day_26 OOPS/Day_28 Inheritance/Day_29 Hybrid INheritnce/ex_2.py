class Hybrid:
    def parent(self):
        print("this is First Parent class")
class B_Class(Hybrid):
    def child_fun(self):
        print("this is Child_Parent class")

class C_class(B_Class):
    def child_c(self):
        print("this C parent and Child")

class D_class(C_class,Hybrid):
    def func_all(self):
        print("all functions accessing")

D = D_class()
D.func_all()
D.child_c()
D.child_fun()
D.parent()

print("="*20)

C = C_class()
C.child_c()
C.child_fun()
C.parent()

print("=-"*20)

B=B_Class()

B_Class().child_fun()
B.parent()

print("=-"*20)

H = Hybrid()
H.parent()