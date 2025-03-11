# data = "hello world"
# print(list(data))
list_val = ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
check = input("enter charecter: ")

if check not in list_val and len(list_val) >= 5:
    print(check, " is available")

else:
    print(check, " is not available ")
