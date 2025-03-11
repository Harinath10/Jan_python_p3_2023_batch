n  = 11
flg  = False
for  i in range(2,n):
    if n % i ==0:
        flg = True
if flg:
    print("Not Prime")
else:
    print("Prime")


