#Without lambda expressions
def a(a,b):
    return a*b

x=a(6,10)
print(x)
                            # here 4 lines code


#with lambda expression
# the syntax is    VARIABLE=lambda a,b:a+b
                #  print(VARIABLE(values)


x=lambda a,b:a*b
print(x(56,2))        #112     # just 2 lines code


x=lambda a,b,c:a*b-c
print(x(56,2,12))      #100


bad=lambda c,d:c%d
print(bad(10,2))        #0