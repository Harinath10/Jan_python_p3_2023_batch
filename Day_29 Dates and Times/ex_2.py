import datetime

print(datetime.datetime(2000,9,18,6,24,28))
val = datetime.datetime(2000,9,18,23,24,28)
print(val.year)
print(val.month)
print(val.day)

print("time --------------------------")

print(val.hour)
print(val.minute)
print(val.second)
print("Perticular date: ",val.date())
print("perticular time: ",val.time())
