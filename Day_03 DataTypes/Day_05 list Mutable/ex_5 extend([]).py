data_list =[10, 20, 90.02, 54j, 11.41, True, 11.41]
print(data_list)
data_list.extend([10,20,30])
print(data_list)

data_list.extend([data_list[0:5:2]])

print(data_list)   # [10, 20, 90.02, 54j, 11.41, True, 11.41, 10, 20, 30, [10, 90.02, 11.41]]