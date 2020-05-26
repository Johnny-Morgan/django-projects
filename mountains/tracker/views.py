from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Avg
from .models import Mountain, Hike
from .forms import MountainForm

def home(request):
    mountains = Mountain.objects.all()
    hikes = Hike.objects.all()

    last_5_mountains = mountains.order_by('-date_climbed')[:5]
    last_5_hikes = hikes.order_by('-hike_date')[:5]

    # height < 300m is a hill
    total_hills = mountains.filter(height__lt=500).count()
    total_mountains = mountains.filter(height__gte=500).count()
    total_hikes = hikes.count()

    context = {'last_5_mountains': last_5_mountains,
               'last_5_hikes': last_5_hikes,
               'total_hills': total_hills,
               'total_mountains': total_mountains,
               'total_hikes': total_hikes}

    return render(request, 'tracker/dashboard.html', context)

def mountains(request):
    mountains = Mountain.objects.all().order_by('-date_climbed')
    total_hills = mountains.filter(height__lt=500).count()
    total_mountains = mountains.filter(height__gte=500).count()
    total = total_hills + total_mountains
    highest_mountain = mountains.order_by('height').last()
    smallest_mountain = mountains.order_by('height').first()

    # Average mountain height
    average_mountain_height = mountains.filter(height__gte=500).aggregate(Avg('height'))['height__avg']
    average_mountain_height = (f'{average_mountain_height:.2f}')
    # Average hill height
    average_hill_height = mountains.filter(height__lt=500).aggregate(Avg('height'))['height__avg']
    average_hill_height = (f'{average_hill_height:.2f}')
    # Average overall height
    average_height = Mountain.objects.aggregate(Avg('height'))['height__avg']
    average_height = (f'{average_height:.2f}')
    
    context = {'mountains': mountains,
               'total_hills': total_hills,
               'total_mountains': total_mountains,
               'total': total,
               'highest_mountain': highest_mountain,
               'smallest_mountain': smallest_mountain,
               'average_height': average_height,
               'average_mountain_height': average_mountain_height,
               'average_hill_height': average_hill_height
               }

    return render(request, 'tracker/mountains.html', context)

def hikes(request):
    hikes = Hike.objects.all().order_by('-hike_date')
    context = {'hikes': hikes}
    return render(request, 'tracker/hikes.html', context)

def peak(request, pk):
    peak = Mountain.objects.get(id=pk)
    context = {'peak':peak}
    return render(request, 'tracker/peak.html', context)

def addMountain(request):
    form = MountainForm()
    if request.method == 'POST':
        print(request.POST)
        form = MountainForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/mountains/')

    context = {'form': form}
    return render(request, 'tracker/add_mountain_form.html', context)

def updateMountain(request, pk):
    mountain = Mountain.objects.get(id=pk)
    form = MountainForm(instance=mountain)

    if request.method == 'POST':
        form = MountainForm(request.POST, instance=mountain)
        if form.is_valid():
            form.save()
            return redirect(f'/peak/{pk}/')
    context = {'form': form}
    return render(request, 'tracker/add_mountain_form.html', context)

def deleteMountain(request, pk):
    mountain = Mountain.objects.get(id=pk)
    if request.method == 'POST':
        mountain.delete()
        return redirect('/')
    context = {'mountain': mountain}
    return render(request, 'tracker/delete.html', context)

def hike(request, pk):
    hike = Hike.objects.get(id=pk)
    context = {'hike':hike}
    return render(request, 'tracker/hike.html', context)