user_name = "Sharath"

pswd = "1234ab"

user_defined_userName = input("enter Your_name :")
user_defined_pswd = input("enter password :")


# if True:
#     print("login SuccessFull")
# else:
#     print("not matched Values")


if user_name == user_defined_userName:
    print("-------------Welcome to XYZ Bank-----------------")
    print("hello MR.",user_name)

    if pswd == user_defined_pswd:
        print("Thankyou",user_name,"login Successfully")

        bank_bal = 5000
        withdrawl_amount= int(input("enter Withdrawl Amount: "))
        if bank_bal >= withdrawl_amount:
            print("withdrawl Sucessfully")
            print("Thanks for visiting.............")
            print("---------Have a Good Day--------- ")
        else:
            print(" Insuffient Funds")
            print(" _______________Please Try Again____________")
    else:
        print(" enter Valid Password!!")

else:
    print("user name and Password Not matched Try again")