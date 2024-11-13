from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from weather import views

router = DefaultRouter()
router.register(r'countries', views.CountryViewSet)
router.register(r'states', views.StateViewSet)
router.register(r'cities', views.CityViewSet)
router.register(r'weather', views.WeatherViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
