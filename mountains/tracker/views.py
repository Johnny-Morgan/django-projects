from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'tracker/dashboard.html')

def mountains(request):
    return render(request, 'tracker/mountains.html')

def hikes(request):
    return render(request, 'tracker/hikes.html')