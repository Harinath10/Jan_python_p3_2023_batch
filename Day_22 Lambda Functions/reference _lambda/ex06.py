#Even number or odd number using lambda

hh=lambda x:True if x%2==0 else False
print(hh(7))        #False

hh=lambda x:"given number is even"  if x%2==0 else "given number is odd"
print(hh(76))

hh=lambda x:"given number is even"  if x%2==0 else "given number is odd"
print(hh(int(input('enter number:: '))))