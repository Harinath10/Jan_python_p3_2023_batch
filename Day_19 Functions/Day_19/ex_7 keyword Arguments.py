# keyword arguments

def student_details(roll_no,name,class_details):
    print("name of the Studnet is :",name)
    print(name , " roll number is :",roll_no)
    print(name ," studied in ",class_details)

student_details(10,"Surjit",5)
student_details(name="Ajith",roll_no=11,class_details=5)
student_details(class_details=6,roll_no=100,name="Vinay")