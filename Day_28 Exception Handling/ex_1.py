# a = 10
# b = 10.0
#
# print(a is c)


try:
    a = 10
    b = 10.0

    print(a is c)
except NameError:
    print("the name of the Variable not available")


print(".........................\n")

try:
    val = 100
    if val ==10:
        print(5/0)
    else:
        print(10/3)
except ZeroDivisionError:
    print("Zero not divisible")
