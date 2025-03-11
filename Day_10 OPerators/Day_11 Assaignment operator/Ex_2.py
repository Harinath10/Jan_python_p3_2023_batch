print("________________OPERATORS ASSAIGN  -=    ______________________")
x = 10
y = 5
z = 7

x -= z    #  x = x-z ==> x = 10 - 7 ==> x= 3
print(x)

y -= x   # y = y - x ==> y = 5 - 3 ==> y = 2
print(y)

z -= (x+y)-12 # z = z-((x+y) - 12 ) ==>  z = z-(x+y) + 12   ==> z = 7 -(5) +12  ==> z = 2+12  ==> z = 14
print(z)

