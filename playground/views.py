from django.shortcuts import render
from django.http import HttpResponse

# def say_hello(request):
#     return HttpResponse("Hello, world! This is a response from the playground app.")

def say_hello(request):
    name = request.GET.get('name', 'Guest')  # default to 'Guest' if not provided
    return HttpResponse(f"Hello, {name}!")

# Create your views here.
