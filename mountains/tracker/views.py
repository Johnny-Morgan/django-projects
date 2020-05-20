from django.shortcuts import render
from django.http import HttpResponse
from .models import Mountain, Hike

def home(request):
    last_5_mountains = Mountain.objects.all().order_by('-date_climbed')[:5]
    last_5_hikes = Hike.objects.all().order_by('-hike_date')[:5]
    context = {'last_5_mountains': last_5_mountains, 'last_5_hikes': last_5_hikes}
    return render(request, 'tracker/dashboard.html', context)

def mountains(request):
    mountains = Mountain.objects.all() 
    context = {'mountains': mountains}
    return render(request, 'tracker/mountains.html', context)

def hikes(request):
    hikes = Hike.objects.all()
    context = {'hikes': hikes}
    return render(request, 'tracker/hikes.html', context)