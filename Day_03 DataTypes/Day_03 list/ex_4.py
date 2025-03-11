s = [1,"h",10,9,7.7,76,9.3,7,7,38,7,92j,"myworld"]

print(s)

res_type = type(s)
print(res_type)
print(len(s))  # 13
print(s.count(76)) # 1
print(s.count(7))   # 3
print(s.count("Solutions"))  # 0


print("-----------------finding index position----------------------")
# finding index position

data = [1,"h",10,9,7.7,76,9.3,7.9,9,7.6,38,7,92j,"myworld"]

print(data.index(92j))
print(data.index(7.7))
print(data.index(7))
