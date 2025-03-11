res = {False, True, 1.2, '30', 10, 11, 6j, 20, 'a', 100, 1000, '10'}
print(res)
print(len((res)))
print(type(res))

res.remove(6j)
print(res)

# res.remove(5000)
# print(res)       # KeyError: 5000