from django.shortcuts import render
#from . models import Features

# Dss Views.
def dss_box(request):
    #dss_box=Features.objects.all{}
    #context={
        #  'dss_box':dss_box
    #}
    return render(request , 'dss_box.html')#, context  )
