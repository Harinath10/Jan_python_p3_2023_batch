from abc import ABC,abstractmethod
class Ipl(ABC):
    @abstractmethod
    def team_acd(self):
        print("Hai,this is Abstract method")
        pass
class Year(Ipl):
    def team_acd(self):
        self.team_name ="CSK"
Y = Year()
Y.team_acd()
print(Y.team_name)
