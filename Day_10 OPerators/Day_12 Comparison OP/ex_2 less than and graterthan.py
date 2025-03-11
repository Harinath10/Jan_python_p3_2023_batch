print("----------------less than ")

a =100
b = 150
c = 24

c += 100


print(a < c)   # True
print(a+b-50 < c+c-100)  # False





s = [1,2,34,"hello","python",10,20,30]
x = ['1',"hello","python","python"]

val = s[0::2]
val_2 = x[0::2]
print(len(val) > len(val_2))   #True
print(len(val)-2 > len(val_2))   # False
print(s[3] == x[3])    # False
print(s[3] != x[3])    # TRue