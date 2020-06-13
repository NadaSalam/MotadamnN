from django.shortcuts import render
#from .models import Cases
from .models import Features
# Create your views here.
'''
def cases(request):
    cases = Cases.objects.all()
    context={
        'cases': cases ,
    }
    return render(request , 'main.html', context)
'''
         #Features Questions

def aoram(request):
    aoram = Features.objects.all()
    context={
        'aoram': aoram ,
    }
    return render(request , 'aoram-ques.html' , context)

            ############################
def burns(request):
        burns = Features.objects.all()
        context={
            'burns': burns ,
        }
        return render(request , 'burns-ques.html' , context )

          ##################################
def clothes(request):
    clothes = Features.objects.all()
    context={
        'clothes': clothes ,
    }
    return render(request , 'clothes-ques.html' , context)

            #################################
def development(request):
    development = Features.objects.all()
    context={
        'development': development ,
    }
    return render(request , 'development-ques.html', context)

              #####################
def economic(request):
    economic = Features.objects.all()
    context={
        'economic': economic ,
    }
    return render(request , 'economic-ques.html', context)

                #####################
def gharmeen(request):
    gharmeen = Features.objects.all()
    context={
        'gharmeen': gharmeen ,
    }
    return render(request , 'gharmeen-ques.html', context)

            ###########################
def heart(request):
    heart = Features.objects.all()
    context={
        'heart': heart ,
    }
    return render(request , 'heart-ques.html', context)
              ########################
def mosneen(request):
    mosneen = Features.objects.all()
    context={
        'mosneen': mosneen ,
    }
    return render(request , 'mosneen-ques.html', context)

         ###################################
def special_people(request):
    special_people = Features.objects.all()
    context={
        'special_people': special_people ,
    }
    return render(request , 'special-people-ques.html', context)

              ##########################
def surgery(request):
    surgery = Features.objects.all()
    context={
        'surgery': surgery ,
    }
    return render(request , 'surgery-ques.html', context)

               #######################
def treatment(request):
    treatment = Features.objects.all()
    context={
        'treatment': treatment ,
    }
    return render(request , 'treatment-ques.html', context)

              #############################
def yeatem(request):
    yeatem = Features.objects.all()
    context={
        'yeatem': yeatem ,
    }
    return render(request , 'yeatem-ques.html', context)
