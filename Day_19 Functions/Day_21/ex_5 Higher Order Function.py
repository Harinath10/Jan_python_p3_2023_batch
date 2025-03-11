# Higher order Functions
# function has a another function as parameter ...
# that function should be return

def first_func(func_2):
    return "this is also function: ",func_2

def p1():
    return "p1 is Second Function"

res = first_func(p1())
print(res)
