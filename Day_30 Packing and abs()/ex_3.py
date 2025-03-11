a,*b,c,d = [11,22,33,44,55,66]
print("value of a:",a)
print("value of b:",b)
print("value of c:",c)
print("value of d:",d)



print("========================")

a,*b,c,d = [11,55,66]
print(a)
print(b)
print(c)
print(d)

print('='*30)

h,*d,f= [i**2 for i in range(10) if i%3==0]
print(d)
print(f)
print(h)

val = []

for i in range(10):
    if i %3 ==0:
        # print(i ** 2)
        val.append(i**2)
print(val)

a1,*a2,a3 = val

print(a1)
print(a2)
print(a3)

print(a1)
print(a2)
print(a3)
