class Media:
    def getMediaInfo(self):
        self.__title=input("Enter Title:")
        self.__price=input("Enter Price:")
    def printMediaInfo(self):
        print(self._title,self._price)
class Magazine(Media):
    def getMagazineInfo(self):
        self.getMediaInfo()
        self.__pages=input("Enter Pages:")
    def printMagazineInfo(self):
        print("Magazine information : ")
        self.printMediaInfo()
        print("Pages:",self.__pages)
class Channel(Media):
    def GetChannelInfo(self):
        self.getMediaInfo()
        self.__freq=input("Enter Frequency:")
    def printChannelInfo(self):
        print("Channel information : ")
        self.printMediaInfo()
        print("Frequency:",self.__freq)

print("Enter Magazine information.")
magzineInfo = Magazine()
magzineInfo.getMagazineInfo()
magzineInfo.printMagazineInfo()

print("Enter Channel information.")
channelInfo = Channel()
channelInfo.GetChannelInfo()
channelInfo.printChannelInfo()