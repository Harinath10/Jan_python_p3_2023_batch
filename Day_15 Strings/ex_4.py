val = "tHis Is PyThon StRing cLaSs"
print(val.find("s"))
print(val.rfind("s"))
print(val.find("S"))
print(val.rfind("S"))

print("index and Slicing \n")
print(val[6])
print(val[-6])
print(val[6::2])
print(val[2::5])

print("starts with and Endswith \n")

print(val.startswith("tHis"))
print(val.startswith("this"))
print(val.startswith("t"))

print(val.endswith("cLaSs"))
print(val.endswith("StRing cLass"))
print(val.endswith("Ss"))