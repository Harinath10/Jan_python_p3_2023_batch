
try:
    val = 100
    if val ==10:
        print(10000/0)
    else:
        print(10/3)
except Exception:
    print("this is Exception Block .... Try block has  exception")


else:
    print("this is Else Block .... Try block has no exception")

finally:
    print("this FInally is Block, if there is  Error Or NOt , Finally always Exicutes")