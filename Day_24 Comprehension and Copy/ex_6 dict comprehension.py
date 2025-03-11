names = ["riyaz","tharun","pawan","lokesh","sreenadh"]

com_1= {each:(len(each)) for each in names}
com= {each:each*(len(each)) for each in names}
print(com_1)

print("----"*15)

com_2= {each:each*(len(each)) for each in names}
print(com_2)

print("----"*15)

string = "aarsfadwsasdasapasrasasad"


com = dict( (each,list(string).count(each)) for each in list(string) )
print(com)