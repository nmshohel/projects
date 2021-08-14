from datetime import datetime

datetime_str = '09-19-18 13:55:26'

a = datetime.strptime(datetime_str, '%m-%d-%y %H:%M:%S')
print(a)
print(type(a))

