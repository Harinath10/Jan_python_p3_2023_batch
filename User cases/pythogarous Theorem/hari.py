ab = eval(input("enter AB Side: "))
bc = eval(input("enter BC Side:"))

ac = 0
res = []
if ab ==bc:
    print("The Side of AC is {}".format(ab))
else:
    ac = ac *2
    ab = ab **2
    bc = bc **2

    ac = ab + bc
    res.append(ac)

final_res = res[0]
convert_complex = complex(final_res)
print(abs(final_res))