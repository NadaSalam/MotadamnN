from django.shortcuts import render , get_object_or_404
from category.models import Category
from category.models import Subcategory
from donation.views import Donation
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


def pay(request):
    
    return render(request , 'pay.html')

def finish(request):
    
    return render(request , 'finished.html')

def about_us(request):

    return render(request , 'about-us.html')


def contact_us(request):

    return render(request , 'contact_us.html')


def news(request):

    return render(request , 'news.html')


def question_answer(request):

    return render(request , 'Q&A.html')    