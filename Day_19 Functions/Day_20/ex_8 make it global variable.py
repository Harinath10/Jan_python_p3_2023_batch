# converting local variable to Global Var

def data():
    global course
    course = ".NET"    # local variable
    print(course)
data()

print(course)