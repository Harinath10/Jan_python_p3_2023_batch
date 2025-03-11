# Without lambda function

def java(a,z):
    return (a-z)
j = java(10,5)
print(j)                        # 5

# With lambda Function

result = lambda a,z :a-z
print(result(10,5))             # 5


print("\n")


result = lambda x,y,z,a :(a+a*(z%y) **a)
print(result(7,8,9,10))             # 5