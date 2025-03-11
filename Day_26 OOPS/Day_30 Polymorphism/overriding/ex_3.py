class Sreenadh:
    def hello_world(self):
        self.name = "Sreenadh"
        self.qua = "Bsc"
        print(self.name,self.qua)
O = Sreenadh()
O.hello_world()
print("---------------------")

class Pavan(Sreenadh):
    def hello_world(self):
        self.a= 10
        self.b = 20
        print(self.a +self.b)

Obj = Pavan()
Obj.hello_world()
Obj.hello_world()