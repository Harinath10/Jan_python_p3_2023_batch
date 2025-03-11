import datetime

present = datetime.datetime.now()

print( present.strftime("%A") )   # Wednesday
print(present.strftime("%a"))     # Wed
print(present.strftime("%D"))     # 03/15/23
print(present.strftime("%d"))     # 15
print(present.strftime("%M"))     # 13
print(present.strftime("%m"))     #  03
print(present.strftime("%C"))     # 20
print(present.strftime("%c"))     # Wed Mar 15 10:13:56 2023
print(present.strftime("%x"))     # 03/15/23
print(present.strftime("%X"))     # 10:14:46
print(present.strftime("%U"))     # we are in 11 th Week of this Year
print(present.strftime("%W"))     # 11
print(present.strftime("%w"))     # 3
