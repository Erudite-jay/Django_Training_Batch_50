from django.http import JsonResponse
from django.shortcuts import render
from .models import User
# Create your views here.

def login_view(request):
    if request.session.get('username'):
        return JsonResponse(
            {
                "success": True,
                "user is": request.session.get('username'),
                "message":"User is already logged in"
            }
           ,status=200
        )
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user=User.objects.get(username=username)
            if user.password == password:
                request.session.set_expiry(20)
                request.session['username'] = username
                return JsonResponse(
                    {
                        "success": True,
                        "message":"User has been logged in successfully"
                    }
                    ,status=200
                )
            else:
                return JsonResponse(
                    {
                        "success": False,
                        "message":"Incorrect password"
                    }
                    ,status=401
                )
        except Exception as e:
            return JsonResponse(
                {
                    "success": False,
                    "message":str(e)
                }
                ,status=500
            )
    
    return render(request, 'Session_app/login.html')