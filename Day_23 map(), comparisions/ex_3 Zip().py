a = [1,2,3,4]
b = [10,20,30,40]
res = zip(a,b)
print(list(res))

#
#
for i,(m,n) in enumerate(zip(a,b)):   # i is index values
    print(i,m+n)                       # m,n Zip values