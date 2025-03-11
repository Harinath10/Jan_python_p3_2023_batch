
# filter(function,sequence)

values = [12,13,15,7,8,12,44]
res =filter(lambda a:a%2==0,values)
print(tuple(res))