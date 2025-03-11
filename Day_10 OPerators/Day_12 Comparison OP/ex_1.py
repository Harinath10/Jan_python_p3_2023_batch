s = [1,2,34,"hello","python"]
x = ['1',"hello","python","python"]

print(len(s) == len(x))   # False
print(len(s)-1 == len(x))  # True

print(s.count("hello") == s.count("python"))   # True
print(s.count("hello") == x.count("python"))   # False

print("----------------not equals to ")
print(s.count("hello") != x.count("python"))   # True


