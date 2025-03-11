# and

a = [1,2,3,4,5]
b = 5


print(len(a) >  4 and 3< a[(4-3 )* 4])
print(len(a) ==  5 and  3 >= a[(4-3 )* 4])
print(len(a[::2]) >1 and (4 *5 -17 <=15))

print("-----------or --------------------------")

print(len(a) ==  5  or 3 >= a[(4-3 )* 4])  #  True or False  ==> True
print(len(a[::2]) >1 or (4 *5 -17 <=15))  # True or True ==> true
print(len(a) <=  4  or 3 >= a[(4-3 )* 4])   # False or FAlse  ==> False

