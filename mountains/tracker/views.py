from django.shortcuts import render
from django.http import HttpResponse
from .models import Mountain, Hike

def home(request):
    mountains = Mountain.objects.all()
    hikes = Hike.objects.all()

    last_5_mountains = mountains.order_by('-date_climbed')[:5]
    last_5_hikes = hikes.order_by('-hike_date')[:5]

    # height < 300m is a hill
    total_hills = Mountain.objects.all().filter(height__lt=300).count()
    total_mountains = Mountain.objects.all().filter(height__gte=300).count()
    total_hikes = hikes.count()

    context = {'last_5_mountains': last_5_mountains, 'last_5_hikes': last_5_hikes,
     'total_hills': total_hills, 'total_mountains': total_mountains, 'total_hikes': total_hikes}

    return render(request, 'tracker/dashboard.html', context)

def mountains(request):
    mountains = Mountain.objects.all() 
    context = {'mountains': mountains}
    return render(request, 'tracker/mountains.html', context)

def hikes(request):
    hikes = Hike.objects.all()
    context = {'hikes': hikes}
    return render(request, 'tracker/hikes.html', context)