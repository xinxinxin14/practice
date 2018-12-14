#_*_ coding:utf-8 _*_
import re
from datetime import datetime,timezone,timedelta

def to_timestamp(dt_str,tz_str):
    dt = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    utc_time = re.match(r'\w{3}([\+|\-])([0-2]?[0-9])\:00$',tz_str)
    print(utc_time)
    Hours = int(utc_time.group(2))
    if utc_time.group(1) == '+':
        new_zone = timezone(timedelta(hours=Hours))
    else:
        new_zone = timezone(timedelta(hours=-Hours))
    return dt.replace(tzinfo=new_zone).timestamp()

# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')

