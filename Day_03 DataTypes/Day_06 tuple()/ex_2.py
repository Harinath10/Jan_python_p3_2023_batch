tuple_val = ('name',0, 'age', 0, 1, 23, 12, 'string',"name")
print(tuple_val)
print(type(tuple_val))  # <class 'tuple'>

print(tuple_val[3])  # 0

res = tuple_val[3]+1  #==> 0 + 1  ==>1
print(tuple_val[res+3])  # ==> res+ 3  ==> 1+3 ==> tuple_val[4]  ==> 1

print(tuple_val[:5:2])  # ('name', 'age', 1)

