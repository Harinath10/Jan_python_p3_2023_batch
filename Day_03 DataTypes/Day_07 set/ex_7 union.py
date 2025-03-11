# union

val_a = {10,5,15}
val_b = {10,"hello",5,"Python"}

print(val_a)
print(val_b)

print("=============")
print(val_a.union(val_b))    # {'Python', 'hello', 5, 10, 15}
print(val_a.intersection(val_b))  # {10, 5}

val_a.clear()

print(val_a)   # set()
