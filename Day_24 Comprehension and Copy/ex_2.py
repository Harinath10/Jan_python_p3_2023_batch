
strs = ['hello', 'and', 'goodbye']

shouting = [s.upper() + '!!!' for s in strs]
## ['HELLO!!!', 'AND!!!', 'GOODBYE!!!']
print(shouting)




print("----------------------------------------")

nums = [2, 8, 1, 6]
small = [ n for n in nums if n <= 2 ]  ## [2, 1]
print(small)

  ## Select fruits containing 'a', change to upper case
fruits = ['apple', 'cherry', 'banana', 'lemon']
afruits = [ s.upper() for s in fruits if 'a' in s ]
  ## ['APPLE', 'BANANA']
print(afruits)


# if  ... else using comprehension


final_var = [(i,"even") if i%2 ==0 else (i,"Odd") for i in range(10)]
print(final_var)



final_var = [(i,"even" if i>5 else (i,"prime")) if i%2 ==0 else (i,"Odd") for i in range(10)]
print(final_var)