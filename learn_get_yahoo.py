from urllib import request
import json

with request.urlopen('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json') as f:
    url_data = f.read().decode('utf-8')
    print(json.loads(url_data))
