class Data(Exception):
    def __init__(self,name):
        self.name = name


def family_mem_count(count):
    if count ==4:
        print("Normal Family ")
    elif count > 4:
        raise Data("Family count is High")
    else:
        raise Data("Family Count is Low")



family_mem_count(2)
