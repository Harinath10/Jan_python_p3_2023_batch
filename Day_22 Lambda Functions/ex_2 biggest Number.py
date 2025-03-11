# def biggest(first =eval(input("first number:")),second = eval(input("second Number")),third= eval(input("third Number:"))):
#     if third < first >second:
#         print(first ,"is a Biggest Number")
#     elif first <second >third:
#         print(second,"is a Biggest Number")
#     else:
#         print(third,"is a Biggest Number")
# biggest()



# With lambda

final_res =lambda a,b :"a is Biggest" if a>b  else ("b is Biggest")
print(final_res(1000,2000))



final_res =lambda a,b,c :"a is Biggest" if a>b and a>c else ("b is Biggest" if b>c and b>a else "c is biggest")
print(final_res(1000,200,30))