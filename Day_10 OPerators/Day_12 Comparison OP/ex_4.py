data = {"A":"manohar","B":"Karthik","C":"Ajith"}

val = data["A"]
key_2 = data["B"]


print(len(val) >= 5)
print(len(key_2) <= 5)
print(len(key_2) != 5)
print(len(key_2) == 5+int(input("enter number:")))
print(len(data["C"]) < 5)    # False
print(len(data["C"]) > 4)    # True
