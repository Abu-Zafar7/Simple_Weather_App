from django.urls import path
from . import views
urlpatterns = [
    path('',views.weather_view,name='weather-view'),
    path('weather/',views.weather_form, name='weather')
]