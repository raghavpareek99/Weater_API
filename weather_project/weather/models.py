from django.db import models

class Country(models.Model):
    country_name = models.CharField(max_length=100, default="Unknown Detail")
    country_code = models.CharField(max_length=3, unique=True)
    continent = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.country_name

class State(models.Model):
    state_name = models.CharField(max_length=100, default="Unknown Detail")
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.state_name

class City(models.Model):
    city_name = models.CharField(max_length=100, default="Unknown Detail")
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    def __str__(self):
        return self.city_name

class Forecast(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    forecast_date = models.DateField()
    temperature_high = models.FloatField()
    temperature_low = models.FloatField()
    weather_description = models.CharField(max_length=255, blank=True, null=True)
    humidity = models.FloatField(blank=True, null=True)
    wind_speed = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.city.city_name} - {self.forecast_date}"
