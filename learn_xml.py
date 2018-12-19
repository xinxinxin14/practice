# _*_ coding:utf-8 _*_
from xml.parsers.expat import ParserCreate
from urllib import request


class DefaultSaxHandler(object):
    def start_element(self,name,attrs):
        print('sax:start_element:%s,attrs:%s'%(name,str(attrs)))


    def end_element(self,name):
        print('sax:end_element:%s'%name)


    def char_data(self,text):
        print('sax:char_data:%s'%text)


xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)


class WeatherSaxHandler(object):
    def __init__(self):
        self.forecast = list()
    def start_element(self,name,attrs):
        if name == 'yweather:location':
           self.country = attrs['country']
           self.city = attrs['city']
        elif name ==  'yweather:forecast':
            self.forecast.append({'date':attrs['date'],'high':attrs['high'],'low':attrs['low']})


    def end_element(self,name):
        pass
    def char_data(self,text):
        pass


def parseXml(xml_str):
    handler = WeatherSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml_str)
    print(handler.forecast)
    return {
        'city': handler.city,
        'forecast': handler.forecast
    }
    
# 测试:
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

with request.urlopen(URL, timeout=4) as f:
    data = f.read()

result = parseXml(data.decode('utf-8'))
assert result['city'] == 'Beijing'
print(result['city'],result['forecast'])
print('ok')
