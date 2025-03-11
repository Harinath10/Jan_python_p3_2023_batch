# Accessing values inside Nested list

x= [10,20,30,(11,2,3,909,[12,34,56,[4,5,67,90],[1,2,3]])]

print(x[3][3])
print(x[3][4][3][3])
print(x[3][4][3][2])
print(x[3][4][4][1])
print(x[3][4][4][-1])

print(x[3][2: 5])