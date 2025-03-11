
# Nested Dictionary
# dictionary parsing


data ={"name":"Pavan",
       "age":[20,30,22,24,24,26],
       "gender":("Male"),
       "Qualification":{"BSC":{"MPCS","MSCS","MECS"},
                        "BBA":"BBA",
                        "B.com":"B.com",
                        "BA":"Btech"},
       "job_role":["SE","SSE"]}

# print(data)
print(type(data))
print(data["name"])
print(data["age"])
print(data["age"][1])
print(data["Qualification"]["BSC"])
print(data["Qualification"]["B.com"])

print("-----------get method --------------------")

print(data.get("NAME"))
print(data.get("Qualification").get("BSC"))
