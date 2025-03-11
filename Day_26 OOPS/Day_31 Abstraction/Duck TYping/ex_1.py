class Bird:
    def fly(self):
        print("Bird can fly and Walk")
class flight:
    def fly(self):
        print("fly with fuel")

class Fish:
    def swim(self):
        print("fish swin in water")

for obj in Bird(),flight():

    obj.fly()

obj_2 = Fish()
obj_2.swim()

