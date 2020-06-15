from django.shortcuts import render
from .models import Charity

                #View Game3 2lMostafeden.
def game3_mostafeden(request):
    game3_mostafeden = Charity.objects.all()
    context={
        'game3_mostafeden': game3_mostafeden ,
    }
    return render(request , 'game3 mostfeden.html', context)

                  #View Gme3 Halat Waiting
def gme3halatwaiting(request):
    gme3halatwaiting = Charity.objects.all()
    context={
        'gme3halatwaiting': gme3halatwaiting ,
    }
    return render(request , 'gme3halatwaiting.html', context)

                      #View Halat Accepted
def halataccepted(request):
    halataccepted = Charity.objects.all()
    context={
        'halataccepted': halataccepted ,
    }
    return render(request , 'halataccepted.html', context)

                     #View Profile Elgm3ia
def profile_elgm3ia(request):
    profile_elgm3ia = Charity.objects.all()
    context={
        'profile_elgm3ia': profile_elgm3ia ,
    }
    return render(request , 'profile-elgm3ia.html', context)

                         #View Add Mostafeden
def add_mostafed(request):
    add_mostafed = Charity.objects.all()
    context={
        'add_mostafed': add_mostafed ,
    }
    return render(request , 'addmostafed.html', context)
