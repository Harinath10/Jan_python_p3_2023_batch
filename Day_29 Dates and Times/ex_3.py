import datetime

print("--------------------Date Only --------------------------")
val_date = datetime.date(1999,9,22)
print(val_date)

print("--------------------Time Only --------------------------")
val_time = datetime.time(3,21,5)
print(val_time)


print("--------------------Combine Both Date and Time --------------------------\n")

combine_d_t = datetime.datetime.combine(val_date,val_time)

print(combine_d_t)