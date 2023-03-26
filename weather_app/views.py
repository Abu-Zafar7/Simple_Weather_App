import requests
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import WeatherSerializer
from .forms import WeatherForm
from api_key import api_key
# Create your views here.

@api_view(['GET'])
def weather_view(request):
    city = request.query_params.get('city','Mumbai')
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key.api_key}&units=metric'
    response = requests.get(url)
    data = {
        'city':city,
        'temperature': response.json()['main']['temp'],
        'weather_description': response.json()['weather'][0]['description']

    }
    serializer = WeatherSerializer(data)
    return Response(serializer.data)

def weather_form(request):
    form = WeatherForm(request.POST)
    weather_data = None
    
    if request.method == "POST":
        if form.is_valid():
            city = form.cleaned_data['city']
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=917b134f9bc2c219dffa24f8f59c2f73&units=metric'
            response = requests.get(url)
            weather_data = {
                'city': city,
                'temperature': response.json()['main']['temp'],
                'weather_description': response.json()['weather'][0]['description']
            }

            return render(request,'weather_app/weather_detail.html',{'weather_data':weather_data,'form':form})
    else: 
        return render(request,'weather_app/weather_detail.html',{'form':form})  