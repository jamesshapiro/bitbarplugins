#!/usr/bin/env PYTHONIOENCODING=UTF-8 /usr/local/bin/python3

# Sunrise / Sunset info courtesy of https://sunrise-sunset.org/api

import sys
sys.path.append('/Users/jamesshapiro/code/bitbarplugins')
import suneventutils

sun_symbol = u'\u263c'
moon_symbol = u'\u263e'
em_dash = u'\u2013'
sunrise_hour, sunrise_minute, sunset_hour, sunset_minute = suneventutils.get_times()

print(f'{sun_symbol} {sunrise_hour}:{sunrise_minute} {em_dash} {sunset_hour}:{sunset_minute} {moon_symbol}')
print('---')
future_sun_events = suneventutils.get_future_sun_events('sunrise')
print('\n'.join(future_sun_events))
