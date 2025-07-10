from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
    path('yes/', views.home, name='home'),
]
    # Add more URL patterns here as needed