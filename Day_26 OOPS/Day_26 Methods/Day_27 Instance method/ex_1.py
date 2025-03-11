class Demo:     # Demo is a Class name
    def data(self):          # data is a Instance method
        self.first_val= 100     # instance V
        self.second_val = 200    # instance V
        print(self.first_val)
        print(self.second_val)

D= Demo()          # Demo() is a Object
D.data()