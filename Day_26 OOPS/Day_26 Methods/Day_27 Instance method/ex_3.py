class Python:        # Classname is Python
    first_val = 100  # class V
    second_val = 200
    sum = first_val + second_val

    def course_details(self):        # it is a instance method ( methodname course_details)
        self.course = "Python"    # instance V
        self.Duration= "3 mon"    # instance V
        print(self.course)
        print(self.Duration)

        # print(a)   # NameError: name 'a' is not defined
        print(self.sum)  # calling class variable with the help of Self

        print("\n")
        print(Python.sum)   # calling class variable with the help of class name



Python().course_details()         # calling instance method help of Obj