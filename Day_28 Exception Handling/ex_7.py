

def empl_sal(sal):
    if sal == 50000:
        print("Sal is Okay")
    elif sal > 50000:
        print("Employee HAppy with this Sal")
    else:
        raise Exception("Sal is Too low")



empl_sal(1000)
