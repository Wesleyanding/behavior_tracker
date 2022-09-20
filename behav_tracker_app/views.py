import json
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

import behav_tracker_app
from .models import Teacher, Class, Student, Behavior
from django.contrib import auth
from django.core import serializers
from .forms import NewBehavForm

from .forms import NewBehavForm
from .models import Behavior

def index(request):
    return render(request, 'behav_tracker_app/index.html')

def students(request):
    return render(request, 'behav_tracker_app/viewstudents.html')

def student_behaviors(request, student_id):
    context = {'student_id': student_id}
    return render(request, 'behav_tracker_app/studentinfo.html', context)

def signup(request):
    if request.method == 'POST':
        Teacher.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password'],
            name=request.POST['name']
        )
        return redirect('behavtrackerapp:login')
    return render(request, 'behav_tracker_app/newteacher.html')

def new_student(request):
    if request.method == 'POST':
        form = request.POST
        newStudent = Student()
        newStudent.name = form.get('name')
        newStudent.grade = form.get('grade')
        newStudent.save()
        teacher_id = form.get('selectedTeacher')
        teacher = Teacher.objects.get(name=teacher_id)
        print(teacher)
        teacher.student.add(newStudent)

        return redirect('behavtrackerapp:index')
    return render(request, 'behav_tracker_app/newstudent.html')

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

def save_behav(request, student_id):
    student = Student.objects.get(name=student_id)

    if request.method == 'POST':
        form = request.POST
        newBehav = Behavior()
        newBehav.antecedent = form.get('antecedent')
        newBehav.behavior = form.get('behavior')
        newBehav.intervention = form.get('intervention')
        newBehav.location = form.get('location')
        newBehav.save()
        student.behavior.add(newBehav)
        student.save()

    return redirect('behavtrackerapp:index')

def view_students(request):
    student_query = Student.objects.all()

    students = []
    for student in student_query:
        students.append({
           'name': student.name
        })

    return JsonResponse(students, safe=False)

def get_behaviors(request, student_id):
    student = Student.objects.get(name=student_id)
    behaviors = list(student.behavior.filter().values('antecedent', 'behavior', 'created_date', 'location', 'intervention'))
    
    return JsonResponse(behaviors, safe=False)

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
