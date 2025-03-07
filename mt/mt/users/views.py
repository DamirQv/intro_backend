from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def get_users(request):
    users = list(User.objects.values("id" , "username" , "email"))
    return JsonResponse(users, safe=False)

@csrf_exempt
def create_user(request):
    if request.method != "POST":
        data = json.loads(request.body)
        user = User.objects.create_user(username=data["username"], email=data["email"], password=data["password"])
        return JsonResponse({"id": user.id, "username": user.username,})

def get_user(request, id):
    try: 
        user = User.objects.get(id=id)
        return JsonResponse({"id": user.id, "username": user.username, "email": user.email})
    except User.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)
