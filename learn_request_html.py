from urllib import request
from html.parser import HTMLParser
from html.entities import name2codepoint
from datetime import datetime
import re


for j in range(1,4): 
    URL =  'https://www.python.org/events/python-events/'+'?page=' +str(j)
    with request.urlopen(URL) as f:
        data = f.read().decode('utf-8')

    event_title = re.findall(r'<a href="/events/python-events/\d{3}/">(.*?)</a>',data)
    event_time = re.findall(r'<time datetime="(.*?)">(.*?) <span class="say-no-more"> (.*?)</span></time>',data)
    event_location = re.findall(r'<span class="event-location">(.*?)</span>',data)
    for i in range(len(event_title)):
        if datetime.strptime(str(event_time[i][0][:10]+event_time[i][0][11:19]),'%Y-%m-%d%H:%M:%S')  > datetime.now():
            print('Upcoming Event:%s,location:%s'%(event_title[i],event_location[i]))
            print('time:%s,%s-%s,%s'%(event_time[i][0],event_time[i][1][:6],event_time[i][1][-7:],event_time[i][2]))
            print('-------------------------------------------------------------------')
