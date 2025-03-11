def pavan(a):
    return  "this is First Function :",a

def srinadh(b,d):
    return "this is 2nd function:",b,d

def saif():
    srinadh(10,20)
    return "last func"

res = pavan(srinadh(saif(),"hello"))
print(res)