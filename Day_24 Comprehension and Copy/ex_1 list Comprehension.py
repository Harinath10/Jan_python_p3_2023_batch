res = [i for i in range(10)]
print(res)    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

res_2 = [i+i for i in range(10)]
print(res_2)



res = []
for i in range(10):
    exp = i+i
    res.append(exp)
print(res)


print("--------------------------------------")

# list comprehensions

res = [data for data in [11,12,13,9,8,7,6]]
print(res)

# without comprehensions

empty_list = []
for i in [11,12,13,9,8,7,6]:
    empty_list.append(i)
print(empty_list)



print("---"*25)

# list Comprehension


b = [10,20,30,2]

result=[res-2*2 for res in b]
print(result)   # [6, 16, 26, -2]