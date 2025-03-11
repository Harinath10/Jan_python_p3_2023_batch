# parameterised Constructer

class Database:
    def __init__(self,name,dur):
        self.dbname = name
        self.duration = dur
        print(self.dbname)
        print(self.duration)
mysql = Database(name=input("enter db name: "),dur=int(input("enter duration in months:")))
postgres = Database(name=input("enter db name: "),dur=int(input("enter duration in months:")))
oracle = Database(name=input("enter db name: "),dur=int(input("enter duration in months:")))

