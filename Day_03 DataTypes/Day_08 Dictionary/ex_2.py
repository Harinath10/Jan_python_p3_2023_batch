# get the values with the help of keys

res = {'a1': '100', 10: '200', 'c1': '300', 'list_val': [10, 20, 30, 40, 40, 60]}

print(res)
print(res["c1"])   # 300
print(res[10])     # 200
print(type(res[10]))  # <class 'str'>
print(res["list_val"])  # [10, 20, 30, 40, 40, 60]

val = res["list_val"]
print(val[-5])    # 20