#!/usr/bin/env PYTHONIOENCODING=UTF-8 /usr/local/bin/python3

# Sunrise / Sunset info courtesy of https://sunrise-sunset.org/api

import requests
import json
import datetime
import pytz

sunrise_api = 'https://api.sunrise-sunset.org/json'

vegas = {'data': {'lat': '36.126634', 'lng': '-115.165729', 'formatted': '0'}, 'timezone': pytz.timezone('America/Los_Angeles')}
dc = {'data': {'lat': '38.996529', 'lng': '-77.027507', 'formatted': '0'}, 'timezone': pytz.timezone('America/New_York')}

location = dc
data = location['data']
tz = location['timezone']

response  = requests.get(sunrise_api, params=location['data'])
result = json.loads(response.text)
sunset = result['results']['sunset']
sunset_time = datetime.datetime.strptime(sunset, "%Y-%m-%dT%H:%M:%S%z")
sunset_time = sunset_time.replace(tzinfo=datetime.timezone.utc).astimezone(tz=tz)
sunset_hour = sunset_time.hour - 12
sunset_minute = sunset_time.minute
moon_symbol = u'\u263e'

sunrise = result['results']['sunrise']
sunrise_time = datetime.datetime.strptime(sunrise, "%Y-%m-%dT%H:%M:%S%z")
sunrise_time = sunrise_time.replace(tzinfo=datetime.timezone.utc).astimezone(tz=tz)
sunrise_hour = sunrise_time.hour
sunrise_minute = sunrise_time.minute
sun_symbol = u'\u263c'

print(f'{moon_symbol} {sunset_hour}:{sunset_minute}PM')
print('---')
print(f'{sun_symbol} {sunrise_hour}:{sunrise_minute}AM')

