from django.shortcuts import render
from .models import Donation
# Create your views here.
# Dss Views.
def donation(request):
    donation = Donation.objects.all()
    context={
          'donation': donation ,
    }
    return render(request , 'dss_box.html' , context)