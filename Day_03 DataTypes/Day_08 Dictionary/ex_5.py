print("------------popitem()---------------------------------")
print("it can remove end of the key")

val = {'a1': '100', 10: '200', 'c1': '300',"d1":"200"}
print(val)
val.popitem()
print(val)
val.popitem()
print(val)

print("------------pop()---------------------------------")
print("it can remove perticular key")

x = {'a1': '100', 10: '200', 'c1': '300',"d1":"200"}
x.pop("a1")
print(x)

