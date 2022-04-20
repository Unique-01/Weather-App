from django.shortcuts import render
import requests
from .forms import CityForm
from .models import City
# from django.db.models.functions import Now
# import datetime
from django.utils import timezone

# Create your views here.

def index(request):
    api = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=f7458c09dfd65d6bdc43c702a9cb376c'
    cities = City.objects.all().order_by('-date_added')
    # now = timezone.now().date()
    # cities = City.objects.filter(date__gte=now).order_by('-date_added')

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    weather_data = []

    for city in cities:
        city_weather = requests.get(api.format(city)).json()

        try:
            weather = {
                'city':city,
                'temperature':city_weather['main']['temp'],
                'description':city_weather['weather'][0]['description'],
                'icon':city_weather['weather'][0]['icon'],
                'pressure':city_weather['main']['pressure'],
                'humidity':city_weather['main']['humidity'],
                'feels_like':city_weather['main']['feels_like'],
                'wind_speed':city_weather['wind']['speed'],
                
            }

        except KeyError:
            weather = None
            print("City Not found")

        else:
            weather = {
                'city':city,
                'temperature':city_weather['main']['temp'],
                'description':city_weather['weather'][0]['description'],
                'icon':city_weather['weather'][0]['icon'],
                'pressure':city_weather['main']['pressure'],
                'humidity':city_weather['main']['humidity'],
                'feels_like':city_weather['main']['feels_like'],
                'wind_speed':city_weather['wind']['speed'],
            }

        
            weather_data.append(weather)
       
    # for city in cities:
    #     city_weather = requests.get(api.format(city)).json()

    #     weather = {
    #         'city':city,
    #         'temperature':city_weather['main']['temp'],
    #         'description':city_weather['weather'][0]['description'],
    #         'icon':city_weather['weather'][0]['icon'],
    #         'pressure':city_weather['main']['pressure'],
    #         'humidity':city_weather['main']['humidity'],
    #         'feels_like':city_weather['main']['feels_like'],
    #         'wind_speed':city_weather['wind']['speed'],
    #     }
    #     weather_data.append(weather)
    
    context = {'weather_data':weather_data,'form':form}

    return render (request,'index.html',context)

