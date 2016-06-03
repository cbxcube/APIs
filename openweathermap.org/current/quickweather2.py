#! python3

# quickweather.py - Prints the weather for a location from the command line.

import json, requests, sys

# Compute location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: quickweather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])

# TODO: Download the JSON data from OpenWeatherMap.org's API.
#url ='http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % (location)
#url ='http://api.openweathermap.org/data/2.5/forecast/city?id=524901&APPID=13c92aaec69963193b975082f7b9436a' % (location)
#url='http://api.openweathermap.org/data/2.5/weather?lat=35&lon=139&&APPID=13c92aaec69963193b975082f7b9436a %(location)'
url='http://api.openweathermap.org/data/2.5/weather?q=Prague&appid=13c92aaec69963193b975082f7b9436a'
response = requests.get(url)
response.raise_for_status()

# TODO: Load JSON data into a Python variable.
#weatherData = json.loads(response.text)
#   # Print weather descriptions.
#   w = weatherData['list']
#   print('Current weather in %s:' % (location))
#   print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
#   print()
#   print('Tomorrow:')
#   print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
#   print()
#   print('Day after tomorrow:')
#   print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
