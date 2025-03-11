first = [2,3,4,5,100]
second = ["hello","world"]
a = 10
b = 10.0
c = 12

res =  ((100 in first or a is 10.0) and (not(a*2 >= 21) and c  is not  12 ))
print(res)

res_2 = not ((100 in first or a is 10.0) and (not(a*2 >= 21) and c  is not  12 ))
print(res_2)