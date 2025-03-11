val = ["a","d",1,2,4,78,True]

print(780 in val)
print(78 in val)
print('a' in val)
print('A' in val)


print("working with tuple ")
val_2 = "a","d",1,2,4,78,True

print("d" in val_2)

print("working with  dict")

s  = {1:"one",2:"two",3:"3"}

print(1 in s)    # True
print("one" in s)  # False