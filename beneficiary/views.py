from django.shortcuts import render

from .models import Beneficiary

def without_img(request):
    without_img = Beneficiary.objects.all()
    context={
        'without_img': without_img ,
    }
    return render(request , 'view-case-without-img.html', context)


def with_img(request):
    with_img = Beneficiary.objects.all()
    context={
        'with_img': with_img ,
    }
    return render(request , 'view-case-with-img.html', context)

