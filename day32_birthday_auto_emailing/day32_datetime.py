import datetime as dt

now = dt.datetime.now()
# print high accuracy time year, month, date, time
print(now)

year = now.year
print(year)

if year == 2022:
    print(type(year))

day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year= 1995,month= 12,day=15)
print(date_of_birth)




