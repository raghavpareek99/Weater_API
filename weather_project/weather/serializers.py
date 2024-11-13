from rest_framework import serializers
from .models import Country, State, City, Forecast

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forecast
        fields = '__all__'
