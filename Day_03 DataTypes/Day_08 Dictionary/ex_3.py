# keys()
# values()
# items()

data = {'a1': '100', 10: '200', 'c1': '300', 'list_val': [10, 20, 30, 40, 40, 60]}
print(data)
print(type(data))

print(data.keys())   #dict_keys(['a1', 10, 'c1', 'list_val'])
print(data.values())  # dict_values(['100', '200', '300', [10, 20, 30, 40, 40, 60]])
print(data.items())   # ([('a1', '100'), (10, '200'), ('c1', '300'), ('list_val', [10, 20, 30, 40, 40, 60])])