# parameterised Constructer

class Database:
    def __init__(self,name,dur):
        self.dbname = name
        self.duration = dur
        print(self.dbname)
        print(self.duration)
db = Database("MYSQL","1 mon")
