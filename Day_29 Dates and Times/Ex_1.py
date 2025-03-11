import datetime
from datetime import date

print("the minimum date is:",date.min)
print("the maximum date is:",date.max)

print(datetime.datetime.now())

present  = datetime.datetime.now()

print('present YEAR Is:',present.year)
print('present Month Is:',present.month)
print('present day Is:',present.day)
print('present hour Is:',present.hour)
print('present min Is:',present.minute)
print('present Second Is:',present.second)




import time
res_2 = time.ctime()
print(res_2)