class Password:
    def set_pswd_datails(self):
        self.pswd = "Hari123@"

    def get_pswd_details(self):
        print(self.pswd)

class User_pswd(Password):
    def all_details(self):
        print(self.pswd)

U = User_pswd()
U.set_pswd_datails()
U.all_details()


print("*^"*25)

class Password:
    def set_pswd_datails(self):
        self.__pswd = "Hari123@"

    def get_pswd_details(self):
        print(self.__pswd)

class User_pswd(Password):
    def all_details(self):
        print(self.__pswd)

U = User_pswd()
U.set_pswd_datails()
U.get_pswd_details()
U.all_details()
