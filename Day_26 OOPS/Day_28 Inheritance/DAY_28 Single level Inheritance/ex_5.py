class Car:
    def car_details(self):
        self.color = "Green_red"
        self.brand= "BMW"
        print(self.color,self.brand)
    def model(self):
        self.year= 2020
        print(self.year)

C = Car()
C.car_details()
C.model()

print("*$_"*20)

class Bike(Car):
    def company(self):
        self.name = "Honda"
        self.price = '140000'
        print(self.name)
        print(self.price)

    def bike_details(self):
        self.milage = "50"
        self.engine = "xyz"
        print(self.milage)
        print(self.engine)

B = Bike()
B.company()
B.bike_details()
print("\n","*"*18)
B.car_details()
B.model()