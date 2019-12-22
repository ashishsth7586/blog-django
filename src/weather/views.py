from django.shortcuts import render
from darksky import forecast
from ipstack import GeoLookup
from datetime import date, timedelta, datetime
import requests
import json


def weather(request):

    geo_lookup = GeoLookup('c4b511b1f75d2bf3fa9b588ae6576d67')
    location = geo_lookup.get_own_location()

    lat = location["latitude"]
    lng = location["longitude"]
    region = location["region_name"]
    city = location["city"]
    country = location["country_name"]

    # Retrieve Weather Data
    weekday = date.today()
    loc = lat, lng
    # with forecast('ae32ed86484ab897ff2ee29d7c2ae1c7', *loc) as loc:
    #     for day in loc.daily:
    #         day = dict(day = date.strftime(weekday, '%a'), sum=day.summary, tempMin=day.temperatureMin, tempMax=day.temperatureMax)
    #         print('{day} ----- {tempMin} ----- {tempMax}'.format(**day))
    #         weekday += timedelta(days=1)

    hour = datetime.now().hour
    location = forecast('ae32ed86484ab897ff2ee29d7c2ae1c7', lat, lng)
    i = 0
    while hour < 24:
        temp = location.hourly[i].temperature
        if hour > 12:
            print('{}pm - {}'.format(hour-12, temp))
        else:
            print('{}am - {}'.format(hour, temp))
        hour += 1
        i += 1

    context = {
        'latitude': lat,
        'longitude': lng,
        'region': region,
        'city': city,
        'country': country,
    }

    return render(request, 'weather.html', context)
    


