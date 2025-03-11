# direct functions no.of loops in functon

# def saif():
#     print("hello python")
#     saif()
# saif()                      #RecursionError: maximum recursion depth exceeded while calling a Python object



import sys

sys.setrecursionlimit(1698)
sys.getrecursionlimit()
a=0
def hai():
    global a
    a=a+1
    print(a)
    hai()
hai()