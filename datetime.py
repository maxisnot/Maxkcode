import datetime

x = datetime.datetime.now()
print(x)
# The date contains year, month, day, hour, minute, second, and microsecond.
x = datetime.datetime.now()
# return the year and name of weekday:
print(x.year)
print(x.strftime("%A"))

x = datetime.datetime(2020, 5, 17)

# To create a date, we can use the datetime() class (constructor) of the datetime module.

# The datetime() class requires three parameters to create a date: year, month, day.
print(x)
