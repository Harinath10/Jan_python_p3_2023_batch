# is
# is not


a = 10
b = 10
h = 5
c  = 10.0
d = "hello"

print(id(a))
print(id(b))

print(id(h))

print(id(c),"<--- this is float 10.0 id")

print("list id Checking--------------------------")

list_f_val = [1,2,3,4]
list_s_val = [1,2,3,4]

print(id(list_f_val))
print(id(list_s_val))



print("tuple id Checking--------------------------")

tuple_f_val = (1,2,3,4)
tuple_s_val = (1,2,3,4)

print(id(tuple_f_val))
print(id(tuple_s_val))



print(id("a"))
print(id("A"))