from datetime import *
today = datetime.today()
print('today is:', today)
for attr in \
['year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond']:
    print(attr, ':\t', getattr(today, attr))
print('time:', today.hour, ':', today.minute, sep='')
day = today.strftime('%a')
month = today.strftime('%b')
print('date:', day, month, today.day)