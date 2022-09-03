from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'behav_tracker_app/index.html')
