import datetime

current_date = datetime.datetime.now()
print(current_date)
past_date = current_date.replace(2002,4,17,5,23,10)
print(past_date)
res =current_date - past_date
print("number of days: ",res)
# #
print(res/365)