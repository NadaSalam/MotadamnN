from django.shortcuts import render

from cases.models import Cases






def all_cases(request):
    all_cases = Cases.objects.all()
    context={
        'all_cases': all_cases ,
    }
    return render(request , 'all cases.html', context)



def home(request):
    home = Cases.objects.all()
    context={
        'home': home ,
    }
    return render(request , 'main.html', context)
