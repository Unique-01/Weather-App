from django.shortcuts import render
import requests
from .forms import CityForm
from .models import City
from decouple import config


# Create your views here.

def index(request):
    # ----------------- Api to assess ----------------------------
    api = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid='+ config('WEATHER_API_KEY')

    # ---------------- City Queryset ---------------------
    cities = City.objects.all().order_by('-date_added')[:5]
    
    # ---------------- Add Form 
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()
    # -------------------- Weather Data for Added Cities
    weather_data = []

    # ------------------- Access Weather Data for cities in database from the API
    for city in cities:
        city_weather = requests.get(api.format(city)).json()

        # ----------------To test if invalid city is entered
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

        # -------------- For all valid cities
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
        
            # ------------- Add the weather to the weather data
            weather_data.append(weather)

    
    context = {'weather_data':weather_data,'form':form}

    return render (request,'index.html',context)

