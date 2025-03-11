# Update --> we can add one or more values

val ={True, 6j, '10', 100, 11, 'a'}
print(val)
print(type(val))
print(len(val))

val.update([10,20,"30",100])
print(val)
print(len(val))

val.update([1000,1.20,True,False])
print(val)