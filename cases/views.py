from django.shortcuts import render
from .models import Cases
# Create your views here.


def all_cases(request):
    all_cases = Cases.objects.all()
    context={
        'all_cases': all_cases ,
    }
    return render(request , 'all cases.html', context)

                  #View Cases card
def card(request):
    card = Cases.objects.all()
    context={
        'card': card ,
    }
    return render(request , 'view-case-card.html', context)

                      #View Cases without img
def without_img(request):
    without_img = Cases.objects.all()
    context={
        'without_img': without_img ,
    }
    return render(request , 'view-case-without-img.html', context)

                     #View Cases without img1
def without_img1(request):
    without_img1 = Cases.objects.all()
    context={
        'without_img1': without_img1 ,
    }
    return render(request , 'view-case-without-img1.html', context)
