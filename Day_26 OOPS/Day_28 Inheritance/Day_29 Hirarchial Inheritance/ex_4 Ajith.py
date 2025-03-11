class Harinath_trainer:
    def _init_(self,Students_names):
        self.stu_name =Students_names

class Dinesh(Harinath_trainer):
    def _init_(self,name,marks):
        self.name =name
        self.marks =marks
        Harinath_trainer._init_(self,"python")

class Kalpana_Roy(Harinath_trainer):
    def _init_(self,name,marks):
        self.name =name
        self.marks =marks
        Harinath_trainer._init_(self,"python")

class Shirisha(Harinath_trainer):
    def _init_(self,name,marks):
        self.name =name
        self.marks =marks
        Harinath_trainer._init_(self,"python")

class Mehaboob(Harinath_trainer):
    def _init_(self,name,marks):
        self.name =name
        self.marks =marks
        Harinath_trainer._init_(self,"Django")

class HariKrishna(Harinath_trainer):
    def _init_(self,name,marks):
        self.name =name
        self.marks =marks
        Harinath_trainer._init_(self,"Django")

class Shuhel(Harinath_trainer):
    def _init_(self,name,marks):
        self.name =name
        self.marks =marks
        Harinath_trainer._init_(self,"Django")

class Ajithkumar(Harinath_trainer):
    def _init_(self,name,marks):
        self.name =name
        self.marks =marks
        Harinath_trainer._init_(self,"MySQL")

Sub1 =Dinesh("A+",95)
Sub2 =Kalpana_Roy("A+",90)
Sub3 =Shirisha("A+",85)

Sub4 = Mehaboob("A+",90)
Sub5 = HariKrishna("A+",85)
Sub6 = Shuhel("A+",95)

Sub7 =Ajithkumar("A",80)

print("Dinesh record is:")
print(Sub1.name,Sub1.marks,Sub1.stu_name)
print()
print("\n")

print("Kalpana_roy record is:")
print(Sub2.name,Sub2.marks,Sub2.stu_name)
print()
print("\n")

print("Shirish record is:")
print(Sub3.name,Sub3.marks,Sub3.stu_name)
print()
print("\n")

print("Mehaboob record is:")
print(Sub4.name,Sub4.marks,Sub4.stu_name)
print()
print("\n")

print("HariKrishna record is:")
print(Sub5.name,Sub5.marks,Sub5.stu_name)
print()
print("\n")

print("Shuhel record is:")
print(Sub6.name,Sub6.marks,Sub6.stu_name)
print()
print("\n")

print("Ajithkumar record is:")
print(Sub7.name,Sub7.marks,Sub7.stu_name)
print()