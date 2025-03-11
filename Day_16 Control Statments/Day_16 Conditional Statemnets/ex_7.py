# data = "hello world"
# print(list(data))
list_val = ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
check = input("enter charecter: ")

if check in list_val or len(list_val) >= 5:
    print(check," is available")

else:
    print(check," is not available ")
