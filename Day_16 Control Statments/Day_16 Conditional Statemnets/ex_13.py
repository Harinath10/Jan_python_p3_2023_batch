x = ["first","second","gender","age","gender"]

if x.count("gender") >= 2:
    print("count of gender length in x  more than 1 ")
    if x[2] =="gender" or len(x[2]) >= 10:
        print("value is matched")
        y = input("enter age:")
        if y == len(x[1]):
            print("age and second lenth matched")
        else:
            corona_cured_candidates_data = int(input("enter recovered patients Number: "))

            if corona_cured_candidates_data <=100:
                print("below 100 recoverd")
            else:
                print("more than 100 recoverd")
    else: print("related gender not matched")

else:
    print("count of gender length in x  less than 1")
