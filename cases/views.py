from django.shortcuts import render

# Create your views here.
from .models import Cases



def all_cases(request):
    all_cases = Cases.objects.all()
    context={
        'all_cases': all_cases ,
    }
    return render(request , 'all cases.html', context)
