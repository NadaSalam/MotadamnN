from django.shortcuts import render
from .models import Cases

# Create your views here.

def cases(request):
    cases = Cases.objects.all()
    context={
        'cases': cases ,
    }
    return render(request , 'main.html', context)
