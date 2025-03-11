# a = [10,20,30]
# print(a[5])
#



try:
    a = [10, 20, 30]
    print(a[5])
except IndexError:
    print("Index out of range")



print(".................\n")

try:
    a = (10, 20, 30)
    a.append(10)
    print(a)
except AttributeError:
    print("Tuple is Immutable , tuple has not append Method")


