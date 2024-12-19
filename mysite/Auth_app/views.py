from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from .models import User
from .serializers import UserSerializer

# Create your views here.

def print_hello_world(request):
    return HttpResponse("hello from backend")

def print_hello_from_template(request):
    return render(request, 'Auth_app/home.html')


def all_data(request):
    if request.method == "GET":
        try:
            all_data=User.objects.all() #queryset -> collection of objects in the form of list
            serializer_data= UserSerializer(all_data,many=True) #serialized data =~ JSON format
            return JsonResponse(serializer_data.data,safe=False) #return
        except Exception as e:
            return JsonResponse({"error":str(e)},status=500)
