# Hierarchical inheritance

# Base class
class Pet:
    def __init__(self,pet_type, name):
        self.pet_type = pet_type
        self.name = name
    def detailes(self):
        print("I am pet")

P1 = Pet('cat','jimmy')
P1.detailes()


# Derived Class 1

class Cat(Pet):
    def _init_(self,pet_type,name):
        self.name = name
        self.pet_type = pet_type

    def detailes(self):
        print('i am cut pet',self.pet_type,'people call me', self.name)

# Derived Class 2

class Dog(Pet):
    def __init__(self,pet_type,name,breed):
        self.name = name
        self.pet_type = pet_type
        self.breed = breed

    def sounds(self,sound):
        return sound
    def detailes(self):
        print(('I am', self.name,'a',self.breed))
P2 = Cat('cat','tinku')
P2.detailes()
P3 = Dog('Dog','Tommy','chow chow')
P3.detailes()
print(P2.name, 'is a chubby',P2.pet_type,"<=======")
print(P3.name,'is a',P3.breed,'and it always',P3.sounds("grow grow"),'<========')