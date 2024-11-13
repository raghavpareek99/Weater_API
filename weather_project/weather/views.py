import datetime
from rest_framework import viewsets
from .models import Country, State, City, Forecast
from .serializers import CountrySerializer, StateSerializer, CitySerializer, WeatherSerializer

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class WeatherViewSet(viewsets.ModelViewSet):
    queryset = Forecast.objects.filter(forecast_date__gte=datetime.date.today()).order_by('forecast_date')[:7]
    serializer_class = WeatherSerializer
