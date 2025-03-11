data = [ "a","b","p",True,6,9.09,77j,"q","b","p",77j]
print(data)
print(len(data))

count = len(data)
print(count+10)

print("---------------slicing-------------------")

val_1 = data[::]
print(val_1)
val_2 = data[ : :1]
print(val_2)
print(data[0::])
print(data[0::1])
print(1*data ,"---------")
print(data[:])


print("---------------slicing-------------------")

print(data[0:5:])  # ['a', 'b', 'p', True, 6]
print(data[2:5:])   # ['p', True, 6]
print(data[4:5:1])   # [6]
print(data[0::1])    # ['a', 'b', 'p', True, 6, 9.09, 77j, 'q', 'b', 'p', 77j]
print(data[0::2])   # ['a', 'p', 6, 77j, 'b', 77j]
print(data[0::3])   # ['a', True, 77j, 'p']
print(data[0::6])    # ['a', 77j]

print(data)
print(data[::-1])   # [77j, 'p', 'b', 'q', 77j, 9.09, 6, True, 'p', 'b', 'a']
print(data[::-2])   # [77j, 'b', 77j, 6, 'p', 'a']
print(data[7:5:-1])

print("-----------------------\n")

print(data[1: -2:])  #
print(data[1: -2:2])  # ['b', True, 9.09, 'q']
print(data[1: -2:3])   #   ['b', 6, 'q']
#
print(data[-5: :])   # [77j, 'q', 'b', 'p', 77j]