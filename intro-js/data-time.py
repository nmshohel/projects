# import datetime
# a='2021-06-01 23:45:00'
# b='2021-06-01 23:50:00'
# print(a)
# print(type(a))
from datetime import datetime, time
then = datetime(2012, 3, 6, 23, 10, 15)        # Random date in the past
then1 = datetime(2012, 3, 5, 23, 5, 15)                          # Now
duration = then - then1  
a='2021-06-01 23:45:00'
b=a.replace("-",",")
c=b.replace(" ", ",")
d=c.replace(":",",")
# print(d)
f=datetime('d')
print(f)


