#without lamda  using if and else

def saif(a,b):
    if a>b:
        print ("true")
    else:
        print('false')
saif(3,4)


def jagga(a,b):
    if a>b:
        return "big is a:",a
    else :
        return "big is b:",b
pqr=jagga(5,7)
print(pqr)



#USING LAMBDA with if and else


#if else statements using lambda
#lambda args: value_to_return "if" condition "else" value_to_return

hari=lambda a,b: a if a>b else b
print(hari(114,783))

amar=lambda a,b,c:a if a>b and a>c else b
print(amar(22,4,5))

amar=lambda a,b,c:a if a>b and a>c else b if b>c else (c,"c is bigger")
print(amar(143,44,53))


amar=lambda a,b,c:("a is biiger",a) if a>b and a>c else (("b is bigger",b) if b>c else (c,"c is bigger"))
print(amar(35,84,563))