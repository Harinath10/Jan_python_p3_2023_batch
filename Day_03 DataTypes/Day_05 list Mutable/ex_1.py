# append()

data = []
print(data)   # []
print(type(data))   # <class 'list'>
data.append(123)
data.append(10)
data.append(12.723j)
print(data)
print(type(data)) # <class 'list'>
print("-----------------------------------------")

value = [10,20,90.02,54j,11.41]
print(len(value))
print(value.count(11.41))
print(value)   # [10, 20, 90.02, 54j, 11.41]
value.append(True)
print(value)   # [10, 20, 90.02, 54j, 11.41, True]
# value.append(12,15)   # TypeError: list.append() takes exactly one argument (2 given)

value.append(11.41)
print(value)
print(value.count(11.41),"<== count of 11.41")





print("-----------------------------------------")



res = [10, 20, 90.02, 54j, 11.41, True, 11.41]
final_value = [12,15,10]
last_value = "twenty"
func= input("enter Values: ")

print(res)
res.append(final_value)
print(res)
res.append(func)
print(res)

# using index




