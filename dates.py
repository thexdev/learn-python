from datetime import datetime

date = datetime.now()

print(date.year)
print(date.strftime('%A'))
print(datetime(2019, 9, 25))
print(date.strftime('%B'))