import os

# print(dir(os))


first_path = "E:\Classes\Jan_python-p3-_2023"
# print(os.getcwd())

# print(first_path)
name ="Day_27 File Handling"    # foldername

print(os.path.join(first_path,name))
path = os.path.join(first_path,name)

# print(path+"\hello")
with open(path+"\data.txt","r") as file_1:
    x = file_1.read()
    print(x)
