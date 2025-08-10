from django.shortcuts import render
from django.http import HttpResponse
# from .sudoku_logic import generate_puzzle

# def say_hello(request):
#     return HttpResponse("Hello, world! This is a response from the playground app.")

def say_hello(request):
    return HttpResponse("Hello!")

# Create your views here.


def home(request):
    # puzzle = generate_puzzle(40)
    return render(request, 'playground/home.html', {'puzzle': puzzle})
