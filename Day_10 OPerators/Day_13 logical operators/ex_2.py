a = 10
b = 10.0
c = 12

print(a*2<21 and c<21 )  # True
print(a*2 > 21 and c <= 12 )  # False
print(a*2 > 21 or c <= 12 ) # True
print(a*2 > 21 or c < 12 ) #  False

print(a*2<21 or a <21 )  # True

print("\n -----------")

print(a == b and b ==a )

res = (a == b and b ==a) and (a*2 > 21 or c <= 12 )

print(res)


res_2 = (a == b and b ==a) and (not(a*2 > 21) and c <= 12 )
print(res_2)

res_3 = (a == b and b ==a) and (not(a*2 > 21) or not(c <= 12)  )
print(res_3)


res_4 = (a == b and b ==a) and (((a*2 > 21) or not(c <= 12) )  and 5<10)
print(res_4)    # False
