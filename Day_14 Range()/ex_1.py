# range ()

data = range(10)     # range(0, 10)
print(data)

data_2 = range(0,10)    # range(0, 10)
print(data_2)

print(list(data))   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(range(10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(tuple(range(int(input("enter range: ")))))
print(tuple(range(int(input("enter starting val:" )),int(input("enter range: ")))))