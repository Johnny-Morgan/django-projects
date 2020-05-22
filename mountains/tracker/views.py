from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Mountain, Hike
from .forms import MountainForm

def home(request):
    mountains = Mountain.objects.all()
    hikes = Hike.objects.all()

    last_5_mountains = mountains.order_by('-date_climbed')[:5]
    last_5_hikes = hikes.order_by('-hike_date')[:5]

    # height < 300m is a hill
    total_hills = Mountain.objects.all().filter(height__lt=500).count()
    total_mountains = Mountain.objects.all().filter(height__gte=500).count()
    total_hikes = hikes.count()

    context = {'last_5_mountains': last_5_mountains, 'last_5_hikes': last_5_hikes,
     'total_hills': total_hills, 'total_mountains': total_mountains, 'total_hikes': total_hikes}

    return render(request, 'tracker/dashboard.html', context)

def mountains(request):
    mountains = Mountain.objects.all().order_by('-date_climbed')
    context = {'mountains': mountains}
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
            return redirect('/')

    context = {'form': form}
    return render(request, 'tracker/add_mountain_form.html', context)