class Parent:

    @staticmethod
    def parent_age():
        age= 25
        age_2 = 30
        age_3 = 27
        print(age)
        print(age_2)
        print(age_3)
    @classmethod
    def parent_gender(cls):
        gender ="F"
        gender_2 ="Female"
        gender_3 ="Male"
        print(gender)
        print(gender_2)
        print(gender_3)

class Child(Parent):
    @staticmethod
    def Child_age():
        print(3)
        print(7)
        print(2)
Child.parent_age()
Child.parent_gender()

Child.Child_age()