from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello ,  name="Sachin"),
]
    # Add more URL patterns here as needed