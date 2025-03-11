a=(5,78,8,535,9083.9,9083,4543,453,967,456,5363,5363.7,8776)
# b=filter(lambda x:x>5000,a)
cat=tuple(filter(lambda x:x>5000,a))
print(cat)
# print(b)


a=(5,78,8,535,9083.9,9083,4543,453,967,456,5363,5363.7,8776)
cat=list(filter(lambda x: x%2==0,a))                                 # these three lines are enough
print("final even numbers in list format is:",cat)                                                          # dont write too much of stuff



          # e r r o r

a=(5,78,8,535,9083.9,9083,4543,453,967,456,5363,5363.7,8776)
b=(9,6,7,3,67,0,6,4,32,11,65,8,9)
# hari=set(filter(lambda x,y:x+y,a)) #hari=set(filter(lambda x,y:x+y>550,a,b))
hari=set(filter(lambda x:x+x>550,a))
print(hari)

                    #TypeError: <lambda>() missing 1 required positional argument: 'y'



x=[1,2,3,3]
p=filter(lambda c:c>2, x)
for s in p:
    print(s)


def hari(xyz):
    k=(6,3,4,2,3,4,1,312,33)
    if( xyz in k):
        return True
    else:
        return False
p=hari(int(input("enter any number")))
print(p)


# def hari(xyz):
#     k=(6,3,4,2,3,4,1,312,33)
#     if( xyz in k):
#         return True
#     else:
#         return False
# p=hari
# print(p(int(input("enter any number"))))


def hari(xyz):
    k=(6,3,4,2,3,4,1,312,33)
    if( xyz in k):
        return "available"
    else:
        return "Not availble",xyz
p=hari(xyz=int(input("enter any number")))
print(p)



def hari(xyz=int(input("enter any number"))):
    k=(6,3,4,2,3,4,1,312,33)
    if( xyz in k):
        return "available"
    else:
        return "Not availble",xyz
p=hari()
print(p)