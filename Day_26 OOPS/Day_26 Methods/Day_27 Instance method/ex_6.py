class Location:
    def root(self,des,km,price):
        self.destination = des
        self.km = km
        self.cost = price


L= Location()
L.root("Hyd",700,1200)
print(L.destination)
print(L.cost)
print(L.km)