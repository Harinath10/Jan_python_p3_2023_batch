class University:
    def university_details(self):
        self.u_name = "SV/JNTU"
        self.loc = "Ap"
    def get_university_details(self):
        print(self.u_name)
        print(self.loc)

class College(University):
    def college_details(self):
        self.C_name = "ABCD"
        self.staff = 28
        self.departments = "4"
    def principal_details(self,name,y_exp):
        self.n = name
        self.y_exp = y_exp
        print(self.n)
        print(self.y_exp)

class Teacher(College):

    def teacher_details(self):
        self.teacher_count = 19
        print(self.teacher_count,"are available")

print("University Object ")

U= University()
U.university_details()
U.get_university_details()

print("==============College Object==================")

C = College()
C.college_details()
C.principal_details("Mohan_Babu",13)

C.university_details()
C.get_university_details()

print("==============Teacher Object==================")

T = Teacher()
T.university_details()
T.get_university_details()

T.principal_details("Gopal",0)
T.college_details()

T.teacher_details()