# acceesing class variable in instance method

class Demo:     # Demo is a Class name
    a = 5000
    y = 2000
    def data(self):          # data is a Instance method
        self.first_val= 100     # instance V
        self.second_val = 200    # instance V
        print(self.first_val)
        print(self.second_val)
        # print(a)  # --> Error
        print(self.a ," <-- accessing class variable with the help of self")
        print(self.y ," <-- accessing class variable with the help of self")
        print("\n")

        print(Demo.a,"<-- accessing class variable with the help of Class Name")
        print(Demo.y,"<-- accessing class variable with the help of Class Name")
D= Demo()          # Demo() is a Object
D.data()
print(Demo.a ,"<--  class V accessing outside the class with the help of classname")
print(Demo.y ,"<--  class V accessing outside the class with the help of classname")