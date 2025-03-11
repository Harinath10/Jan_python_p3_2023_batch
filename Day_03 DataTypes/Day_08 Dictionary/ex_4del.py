val = {'a1': '100', 10: '200', 'c1': '300',"a1":6000}
print(val)

data = {True:"hello",1:10000}

print(data)


del val["c1"]
print(val)

val.clear()
print(val)
print(type(val))
