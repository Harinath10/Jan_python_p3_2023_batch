# method Overriding

class College:
    def students(self):
        self.numer_of_students_in_10 = 250
        self.numer_of_students_in_6 = 20
        self.numer_of_students_in_Clg = 700
        print(self.numer_of_students_in_10,self.numer_of_students_in_6,self.numer_of_students_in_Clg)

class School(College):
    def students(self):
        self.teachers_count = 12
        self.students_count = 352
        print("number of teachers in School is :",self.teachers_count)
        print("number of students in School is :",self.students_count)

S= School()
S.students()
print("\n")
S.students()
print("\n")
S.students()

print("\n")

College().students()