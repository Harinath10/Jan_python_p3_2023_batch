class Doctor:

    def count(self):
        self.count_doc= 12

    def count_details(data):
        print(data.count_doc)

class Patient(Doctor):
    def patient_count(self):
        self.count_num = 211
        print(self.count_num)
P = Patient()
P.patient_count()
P.count()
P.count_details()

class Chairmen(Patient):
    def name(self):
        self.name_c= "Abdc"
        print(self.name_c)
controller = Chairmen()
print("\n")
controller.count()
controller.count_details()
# controller.patient_count()
controller.name()

class Final_one(Patient):
    def data(self):
        print("this  is Final Data")

print("\n")
F = Final_one()
F.data()
F.patient_count()
F.count()
F.count_details()