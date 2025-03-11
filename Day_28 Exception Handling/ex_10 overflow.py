import traceback
j = 5.0


try:
    for i in range(1, 1000):
        j = j**i
        print(j)
except OverflowError as e:
    print("Overflow error happened")
    print(f"{e}, {e.__class__}")

