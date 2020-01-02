#!/usr/bin/env PYTHONIOENCODING=UTF-8 /usr/local/bin/python3

# Sunrise / Sunset info courtesy of https://sunrise-sunset.org/api

import requests
import json
import datetime
import pytz

sunevent_api = 'https://api.sunrise-sunset.org/json'

date = datetime.datetime.now()

current_year = date.year
current_month = date.month
current_day = date.day

locations = {
    'vegas': {
        'data': {
            'lat': '36.126634', 'lng': '-115.165729', 'formatted': '0'
        }, 'timezone': pytz.timezone('America/Los_Angeles')
    },
    'dc': {
        'data': {
            'lat': '38.996529', 'lng': '-77.027507', 'formatted': '0'
        }, 'timezone': pytz.timezone('America/New_York')
    }
}

desired_location = 'vegas'
em_dash = u'\u2013'

def get_time(result, sun_event, tz):
    sun_event_iso8601 = result['results'][sun_event]
    sun_event_utc = datetime.datetime.strptime(sun_event_iso8601, "%Y-%m-%dT%H:%M:%S%z")
    sun_event_local = sun_event_utc.replace(tzinfo=datetime.timezone.utc).astimezone(tz=tz)
    sun_event_hour = sun_event_local.hour
    if sun_event == 'sunset':
        sun_event_hour = sun_event_hour - 12
    sun_event_minute = sun_event_local.minute
    return sun_event_hour, '0' + str(sun_event_minute) if sun_event_minute < 10 else sun_event_minute

def get_times(
        location=desired_location,
        date=f'{current_year}-{current_month}-{current_day}'):
    location = locations[location]
    data = location['data']
    data['date'] = date
    tz = location['timezone']
    response  = requests.get(sunevent_api, params=data)
    result = json.loads(response.text)
    sunrise_hour, sunrise_minute = get_time(result, 'sunrise', tz)
    sunset_hour, sunset_minute = get_time(result, 'sunset', tz)
    return sunrise_hour, sunrise_minute, sunset_hour, sunset_minute

def get_future_sun_events(sun_event='sunrise'):
    num_days = [7,14,30,60,90,180]
    text = [f'In {days} days:' for days in num_days]
    result = []
    for num_days, message in zip(num_days, text):
        future_date = datetime.datetime.now() + datetime.timedelta(days=num_days)
        future_year =  future_date.year
        future_month = future_date.month
        future_day = future_date.day
        sunrise_hour, sunrise_minute, sunset_hour, sunset_minute = get_times(
            date=f'{future_year}-{future_month}-{future_day}')
        result.append(f'{message} {sunrise_hour}:{sunrise_minute} AM {em_dash} {sunset_hour}:{sunset_minute} PM')
    return result
