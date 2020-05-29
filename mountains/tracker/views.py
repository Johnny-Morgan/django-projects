from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Avg, Sum
from .models import Mountain, Hike
from .forms import MountainForm, HikeForm

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
    average_mountain_height = f'{average_mountain_height:.2f}'
    # Average hill height
    average_hill_height = mountains.filter(height__lt=500).aggregate(Avg('height'))['height__avg']
    average_hill_height = f'{average_hill_height:.2f}'
    # Average overall height
    average_height = Mountain.objects.aggregate(Avg('height'))['height__avg']
    average_height = f'{average_height:.2f}'
    
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
    total_hikes = hikes.count()

    # total length of hike
    total_length = Hike.objects.aggregate(Sum('length'))['length__sum']
    total_length = f'{total_length:.2f}'

    # average length of hike
    average_length = float(total_length) / total_hikes
    average_length = f'{average_length:.2f}'

    # total ascent
    total_ascent = Hike.objects.aggregate(Sum('total_ascent'))['total_ascent__sum']
    total_ascent = f'{total_ascent:.2f}'

    # average ascent
    average_ascent = float(total_ascent) / total_hikes
    average_ascent = f'{average_ascent:.2f}'

    # total descent
    total_descent = Hike.objects.aggregate(Sum('total_descent'))['total_descent__sum']
    total_descent = f'{total_descent:.2f}'

    # average descent
    average_descent = float(total_descent) / total_hikes
    average_descent = f'{average_descent:.2f}'
    
    # total time
    hikes = Hike.objects.all().order_by('-hike_date')
    hours = 0
    minutes = 0
    seconds = 0
    for hike in hikes:
        hours += int(hike.duration.split(':')[0])
        minutes += int(hike.duration.split(':')[1])
        seconds += int(hike.duration.split(':')[2])
    minutes += seconds // 60
    seconds %= 60
    hours += minutes // 60
    minutes %= 60
    total_time = f'{hours}:{minutes}:{seconds}'
    
    # average time
    total_seconds = seconds + minutes * 60 + hours * 3600
    average_seconds = total_seconds / total_hikes
    average_time = average_seconds / 3600
    average_time = f'{average_time:.2f}'

    # average speed
    average_speed = (float(total_length) / total_hikes) / (average_seconds / 3600)
    average_speed = f'{average_speed:.2f}'

    context = {'hikes': hikes,
               'total_hikes': total_hikes,
               'total_length': total_length,
               'average_length': average_length,
               'total_ascent': total_ascent,
               'average_ascent': average_ascent,
               'total_descent': total_descent,
               'average_descent': average_descent,
               'total_time': total_time,
               'average_time': average_time,
               'average_speed': average_speed,
               }
               
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
        return redirect('/mountains/')
    context = {'mountain': mountain}
    return render(request, 'tracker/delete.html', context)

def hike(request, pk):
    hike = Hike.objects.get(id=pk)
    context = {'hike':hike}
    return render(request, 'tracker/hike.html', context)

def addHike(request):
    form = HikeForm()
    if request.method == 'POST':
        print(request.POST)
        form = HikeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/hikes/')

    context = {'form': form}
    return render(request, 'tracker/add_hike_form.html', context)

def updateHike(request, pk):
    hike = Hike.objects.get(id=pk)
    form = HikeForm(instance=hike)

    if request.method == 'POST':
        form = HikeForm(request.POST, instance=hike)
        if form.is_valid():
            form.save()
            return redirect(f'/hike/{pk}/')
    context = {'form': form}
    return render(request, 'tracker/add_hike_form.html', context)

def deleteHike(request, pk):
    hike = Hike.objects.get(id=pk)
    if request.method == 'POST':
        hike.delete()
        return redirect('/hikes/')
    context = {'hike': hike}
    return render(request, 'tracker/delete_hike.html', context)