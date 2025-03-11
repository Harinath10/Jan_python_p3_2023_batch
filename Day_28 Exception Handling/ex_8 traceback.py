import traceback



try:
    val = 10
    if val ==10:
        print(5/0)
    else:
        print(10/3)
except Exception:
    print("this is Exception Block .... Try block has  exception")
    print("Zero not divisible")
    # traceback.print_exc()