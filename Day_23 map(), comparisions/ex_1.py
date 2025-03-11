# map without lambda

def f1(a,b,c,d):
    return a+b+c+d

res = map(f1,[1,2,3,5],[1,1,12,13],[21,23],[5,6,7,8,10])
print(list(res))

res_2 = tuple(map(f1,[12,35],[10,112],[21,23],[567,810]))
print(res_2)