val = (1,11,21,31,1.98,"string",False,False,False)

print(type(val))
print(len(val))
res = val.count(False)

print(res//3)


print(val.index(31)-5)

print(val[val.index(31)-5])



print("----------------immutable")
print(val)
val.append(90)
print(val)


