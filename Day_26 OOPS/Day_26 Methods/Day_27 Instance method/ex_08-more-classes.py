class A:  # first class --a
    def __init__(self):
        self.ticketbooking = 0
        self.cost = 3500


fa = A()
print(fa.ticketbooking)
print(fa.cost)

print("\n")


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

class A1:
    def __init__(self):
        self.patient = "bharath"
        self.disease = "feVeR"
        self.age = 56
        self.b2 = []

    def omega(self, b2):
        self.b2.append(b2)


class b2:
    def __init__(self):
        self.id = 17898
        self.location = "chinthaparthi"


rbit = A1()
print(rbit.patient.title())
print(rbit.disease.swapcase())
print(rbit.age)

sbit = b2()
rbit.omega(sbit)
for x in rbit.b2:
    print(x.id)
    print(x.location.upper())

print("\n")


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

class abc:  # first class--abc
    def __init__(self, holdername, accountType):
        self.hN = holdername
        self.aT = accountType
        self.df = []

    def orbit(self, dde):
        self.df.append(dde)


class df:  # SECOND class--df
    def __init__(self, hage, hGuardianName):
        self.age = hage
        self.gName = hGuardianName


yvkota = abc("santhamma", "savings")
print("HOLDER NAME: ", yvkota.hN.upper())
print("ACCOUNT TYPE: ", yvkota.aT)

bjpalli = df(49, "raghunath")

yvkota.orbit(bjpalli)

for i in yvkota.df:
    print(i.age)
    print(i.gName)

print("\n")


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

class abc:  # first class--abc
    def __init__(self, holdername, accountType):
        self.hN = holdername
        self.aT = accountType
        self.df = []
        self.mno = []

    def omega(self, ok):
        self.df.append(ok)

    def wah(self, nop):
        self.mno.append(nop)


class df:  # SECOND class--df
    def __init__(self, hage, hnominee):
        self.age = hage
        self.nominee = hnominee


class mno:  # Third class--mno
    def __init__(self, nage, nrelaion):
        self.age = nage
        self.relation = nrelaion


amitta = abc('kamalakar', "current")
print("HOLDER NAME: ", amitta.hN)
print("ACCOUNT TYPE: ", amitta.aT)

knagar = df(41, "sujatha")
bcolony = mno(36, "WIFE")

amitta.omega(knagar)
amitta.wah(bcolony)

for i in amitta.df:
    print("HOLDER AGE: ", i.age)
    print("HOLDER NOMINEE NAME: ", i.nominee)
for g in amitta.mno:
    print("NOMINEE AGE: ", g.age)
    print("NOMINEE RELATION: ", g.relation)


##############################################################################
class Dates:
    def __init__(self, date):
        self.dat = date

    def getDate(self):
        return self.dat

    @staticmethod
    def toDashDate(dae):
        return dae.replace("/", "-")


d = Dates("15-12-2016")
dateFromDB = "15/12/2006"
dateWithDash = Dates.toDashDate(dateFromDB)

if (d.getDate() == dateWithDash):
    print("Equal")
else:
    print("Unequal")
