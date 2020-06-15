from django.shortcuts import render
from .models import Donor

# Donor profile

def profile (request):
    profile = Donor.objects.all()
    context={
        'profile': profile ,
    }
    return render(request , 'profile-donor.html' , context)
