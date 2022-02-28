from django.urls import path
from . import views

# URL configuration modul
urlpatterns = [
    path('hello/', views.say_hello)
]