
f_write = open("sample.txt","w")
statement = input("enter some data: ")
f_write.write(statement)
f_write.close()


n = open("sample.txt","r")
res=n.read()
print(res)

