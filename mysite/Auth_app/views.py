from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def print_hello_world(request):
    return HttpResponse("hello from backend")

def print_hello_from_template(request):
    return render(request, 'Auth_app/home.html')