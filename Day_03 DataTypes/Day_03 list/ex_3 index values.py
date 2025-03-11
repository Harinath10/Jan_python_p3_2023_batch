s = [1,"h",10,9,7.7,76,9.3,7,7,38,7,92j,"myworld"]

print(s)

res_type = type(s)
print(res_type)

print("-------------------find value using index psoition ------------------")
print(s[0])   # 1
print(s[1])  # h
print(s[2])   # 10
print(s[3])   # 9
print(s[4])    # 7.7
print(s[5])   # 76
print(s[6])   # 9.3
print(s[7])  # 7
print(s[8])  #7
print(s[9])  # 38
print(s[10]) # 7
print(s[11])   # 92j
print(s[12])  # myworld
print(s[10])  # 7
print("-----------------")
# print(s[13])   # IndexError: list index out of range

print("-------Negative----------")

print(s[-1])   # 'myworld'
print(s[-2])   # 92j
print(s[-3])   # 7
print(s[-4])
print(s[-5])
print(s[-6])
print(s[-7])