import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Teacher, Class, Student, Behavior
from django.contrib import auth

def index(request):
    teachers = Teacher.objects.all()
    context = {
        'teachers': teachers
    }
    return render(request, 'behav_tracker_app/index.html', context)

def login(request):
    if request.method == "GET":
        return render(request, "behav_tracker_app/login.html")
    elif request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username", "")
        password = data.get("password", "")

        user = auth.authenticate(request, username=username, password=password)
        if user == None:
            return JsonResponse({"message": "Invalid username or password."})
        else:
            auth.login(request, user)
            return JsonResponse({"message": "ok"})
