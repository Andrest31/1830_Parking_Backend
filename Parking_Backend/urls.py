from Parking import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.HelloPage),
    path('parking/', views.MainPage),
    path('hello/', views.ParkingPage),
    path('hello/', views.PassPage),
]
