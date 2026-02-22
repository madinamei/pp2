#datetime
import datetime

x = datetime.datetime.now()
print(x)

import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

import datetime

now = datetime.now()
print(now)

import date

today = date.today()
print(today)

#creating date objects
import datetime

x = datetime.datetime(2020, 5, 17)

print(x)

import date

d1 = date(2026, 2, 22)
print(d1)

import date

today = date.today()
print(today)

import date

year = 2025
month = 12
day = 31

d2 = date(year, month, day)
print(d2)
#date formatting
import datetime

now = datetime.now()
print(now.strftime("%Y-%m-%d"))

print(now.strftime("%d/%m/%Y"))

print(now.strftime("%B %d, %Y"))

print(now.strftime("%b %d, %y"))

print(now.strftime("%Y-%m-%d %H:%M:%S"))
#calculating time differences
from datetime import date

date1 = date(2026, 1, 1)
date2 = date(2026, 2, 22)

difference = date2 - date1
print(difference.days)

from datetime import datetime

t1 = datetime(2026, 2, 22, 10, 0, 0)
t2 = datetime(2026, 2, 22, 15, 30, 0)

difference = t2 - t1
print(difference)

print(difference.total_seconds())

from datetime import datetime

start = datetime(2026, 2, 20, 8, 0)
end = datetime(2026, 2, 22, 10, 30)

diff = end - start

print("Days:", diff.days)
print("Seconds:", diff.seconds)
print("Total hours:", diff.total_seconds() / 3600)
#working with time zones

from datetime import datetime
from zoneinfo import ZoneInfo

dt = datetime(2026, 2, 22, 12, 0, tzinfo=ZoneInfo("UTC"))
print(dt)

from datetime import datetime
from zoneinfo import ZoneInfo

utc_time = datetime(2026, 2, 22, 12, 0, tzinfo=ZoneInfo("UTC"))
almaty_time = utc_time.astimezone(ZoneInfo("Asia/Almaty"))

print("UTC:", utc_time)
print("Almaty:", almaty_time)

from datetime import datetime
from zoneinfo import ZoneInfo

tokyo_time = datetime.now(ZoneInfo("Asia/Tokyo"))
print(tokyo_time)