
try:
    val = 10
    if val ==10:
        print(5/0)
    else:
        print(10/3)
except ZeroDivisionError:
    print("this is Exception Block .... Try block has  exception")
    print("Zero not divisible")

else:
    print("this is Else Block .... Try block has no exception")
