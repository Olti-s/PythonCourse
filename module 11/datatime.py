import datetime

current_date=datetime.datetime.now()
print(current_date.year)
print(current_date.month)
print(current_date.date())
print(current_date.second)


current_time=datetime.datetime.now().time()
print(current_time)

current_time1=datetime.datetime.now().date()
print(current_time1)