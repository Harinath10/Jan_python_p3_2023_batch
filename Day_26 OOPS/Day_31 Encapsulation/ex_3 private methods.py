# MAngling

class Data:

    def __value(self):              # private Method
        self.first_value = "100 "
        self.second_value = "20"

    def __get_value(self):
        res = self.first_value + self.second_value
        print(res)
        print(type(res))

D = Data()            # Object Creation
# D.__value()
# D.__get_value()

# mangling
D._Data__value()
D._Data__get_value()
#
#
#
print("*-="*20 ,"\n")

# MAngling

class Data:

    def __value(self,value_1,value_2):              # private Method
        self.first_value = value_1
        self.second_value = value_2

    def __get_value(self):
        res = self.first_value + self.second_value
        print(res)
        print(type(res))

D = Data()            # Object Creation
# D.__value()
# D.__get_value()

D._Data__value("python ","Sql")
D._Data__get_value()

D._Data__value(5,10)
D._Data__get_value()


D._Data__value(True,False)
D._Data__get_value()

#
#
