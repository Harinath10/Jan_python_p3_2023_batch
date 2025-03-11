with open("Student_details.csv", "r") as first_file:
    d =first_file.read()
    print(d)

with open("sample.txt","w") as first_file:
    values = "hello \n" \
             "world\n" \
             "hello \t" \
             "python"
    d =first_file.write(values)
    print(d)