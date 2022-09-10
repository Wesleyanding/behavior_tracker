import json
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Teacher, Class, Student, Behavior
from django.contrib import auth
from django.core import serializers

def index(request):
    return render(request, 'behav_tracker_app/index.html')

def get_teachers(request):
    teachers_query = Teacher.objects.all()

    teachers = []
    for teacher in teachers_query:
        teachers.append({
            'name': teacher.name,
            'classes': list(teacher.classes.filter().values('name')),
            'students': list(teacher.student.filter().values('name'))
        })

    return JsonResponse(teachers, safe=False)

def get_student(request, student_id):
    student = Student.objects.get(name=student_id)
    behaviors = list(student.behavior.filter().values('antecedent', 'behavior', 'created_date', 'location', 'intervention'))
    return JsonResponse({'data': behaviors})

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

def logout(request):
    auth.logout(request)
    return redirect('behavtrackerapp:login')
