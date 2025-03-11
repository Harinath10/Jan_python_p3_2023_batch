res = {False, True, 1.2, '30', 10, 11, 6j, 20, 'a', 100, 1000, '10'}
print(res)
print(len((res)))
print(type(res))

res.discard(False)
print(res)

res.discard(1000)
print(res)

res.discard(7000)
print(res,"============")