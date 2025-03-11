# map()
# map(function ,iterables)
first_values = [1,2,3,4]
sec_values = [10,20,30,40]

V = map(lambda x,y : x+y ,first_values,sec_values)
print(tuple(V))

res = map(lambda x,y : x-y ,first_values,sec_values)
final_res = list(res)
final_res.append(100)
print(final_res)
