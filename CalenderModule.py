import calendar
import datetime

m,d,y = map(int,input().split())
print(m,d,y)
input_date = datetime.date(y,m,d)
print(input_date)
print(calendar.day_name[input_date.weekday()].upper())
