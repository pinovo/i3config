#!/usr/bin/env python

import requests
import json

url = 'https://api.met.no/weatherapi/locationforecast/2.0/compact?altitude=535&lat=49.31&lon=16.15'

headers = {
    'User-Agent': 'Linux Weather i3bar applet',
    'From': 'pin2k.cz@gmail.com.com'  # This is another valid field
}

response = requests.get(url, headers=headers)
r = response.json()
print(r['properties']['timeseries'][0]['data']['instant']['details']['air_temperature'],'°C')
