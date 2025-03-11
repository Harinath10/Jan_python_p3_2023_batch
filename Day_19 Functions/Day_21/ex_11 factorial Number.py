def fact(number= int(input("enter fact number:"))):
    result = 1
    while number > 0:
        result = result * number   #result *= number
        number = number - 1          # number -= 1
    return result
res = fact()
print(res)


