if False:
    print("if is false")
    print("if not work")

elif False:
    print("first elif also False")
elif True:
    x = ["first", "second", "gender", "age", "gender"]

    if x.count("gender") >= 2:
        print("count of gender length in x  more than 1 ")
        if x[2] == "gender" or len(x[2]) >= 10:
            print("value is matched")
    print("this Elif block executes")
elif False:
    print("third elif also not work")
else:
    print("if above all conditions False ,This Block will execute")