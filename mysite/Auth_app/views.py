from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def print_hello_world(request):
    return HttpResponse("hello from backend")

def print_hello_from_template(request):
    return render(request, 'Auth_app/home.html')


@csrf_exempt
def all_data(request):
    if request.method == "GET":
        try:
            all_data=User.objects.all() #queryset -> collection of objects in the form of list
            serializer_data= UserSerializer(all_data,many=True) #serialized data =~ JSON format
            return JsonResponse(serializer_data.data,safe=False) #return
        except Exception as e:
            return JsonResponse({"error":str(e)},status=500)
    
    if request.method == "POST":
        try:
            input_data=json.loads(request.body) #from frontend side / client side
            serializer_data=UserSerializer(data=input_data) #converted data
            if serializer_data.is_valid(): #validation
                serializer_data.save()
                return JsonResponse({"message":"Data saved successfully"},status=201)
            else:
                return JsonResponse(serializer_data.errors,status=400)
        except Exception as e:
            return JsonResponse({"error":str(e)},status=500)

@csrf_exempt
def single_user_data(request,pk):
    if request.method == "GET":
        try:
            user_data=User.objects.get(pk=pk) #get single object
            serializer_data=UserSerializer(user_data) #serialized data
            return JsonResponse({
                "data":serializer_data.data
            },status=200)
        except User.DoesNotExist:
            return JsonResponse({"error":"User not found"},status=404)
        except Exception as e:
            return JsonResponse({"error":str(e)},status=500)
    
    if request.method == "PUT":
        try:
            input_data=json.loads(request.body)
            user=User.objects.get(pk=pk)

            serializer_data=UserSerializer(user,data=input_data)
            if serializer_data.is_valid():
                serializer_data.save()
                return JsonResponse({"message":"Data updated successfully"},status=200)
            else:
                return JsonResponse(serializer_data.errors,status=400)
        except User.DoesNotExist:
            return JsonResponse({"error":"User not found"},status=404)
        except Exception as e:
            return JsonResponse({"error":str(e)},status=500)
        
    if request.method == "DELETE":
        try:
            user=User.objects.get(pk=pk)
            user.delete()
            return JsonResponse({"message":"Data deleted successfully"},status=204)
        except User.DoesNotExist:
            return JsonResponse({"error":"User not found"},status=404)
        except Exception as e:
            return JsonResponse({"error":str(e)},status=500)
        
    if request.method == "PATCH":
        try:
            input_data=json.loads(request.body)
            user=User.objects.get(pk=pk)

            serializer_data=UserSerializer(user,data=input_data,partial=True) #partial update
            if serializer_data.is_valid():
                serializer_data.save()
                return JsonResponse({"message":"Data updated successfully"},status=200)
            else:
                return JsonResponse(serializer_data.errors,status=400)
        except User.DoesNotExist:
            return JsonResponse({"error":"User not found"},status=404)
        except Exception as e:
            return JsonResponse({"error":str(e)},status=500)