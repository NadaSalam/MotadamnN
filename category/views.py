from django.shortcuts import render
from .models import Category

def all_programs(request):
    return render(request ,'category/index.html')

def development(request):
    return render(request ,'category/development.html')

def economic_support(request):
    return render(request ,'category/economic_support.html' )

def medical(request):
    return render(request ,'category/medical.html' )

def social_support(request):
    return render(request ,'category/social support.html' )

def zakat(request):
    return render(request ,'category/zakat.html' )

def addiction(request):
    return render(request ,'category/addiction.html' )

def tumor(request):
    return render(request ,'category/aoram.html' )

def baby(request):
    return render(request ,'category/babies.html')

def blind(request):
    return render(request ,'category/blind.html' )

def blind_diseas(request):
    return render(request ,'category/blind2.html' )

def accident_burns(request):
    return render(request ,'category/burns.html' )

def virus_c(request):
    return render(request ,'category/c_virus.html' )

def cancer(request):
    return render(request ,'category/cancer.html' )

def children(request):
    return render(request ,'category/children.html' )

def cow(request):
    return render(request ,'category/cow.html' )

def clothes(request):
    return render(request ,'category/clothes.html' )

def artificial_limps(request):
    return render(request ,'category/devices.html' )

def food(request):
    return render(request ,'category/food.html' )

def deptors(request):
    return render(request ,'category/gharmeen.html' )

def good_loan(request):
    return render(request ,'category/good-loan.html' )

def heart(request):
    return render(request ,'category/heart.html' )

def house(request):
    return render(request ,'category/house.html' )

def jop(request):
    return render(request ,'category/job.html' )

def kidny(request):
    return render(request ,'category/kidny.html' )

def charity_project(request):
    return render(request ,'category/mashare3.html' )

def old_people(request):
    return render(request ,'category/mosneen.html' )

def ray(request):
    return render(request ,'category/ray.html' )

def special_people(request):
    return render(request ,'category/special-people.html' )

def surgery(request):
    return render(request ,'category/surgery.html' )

def treatment(request):
    return render(request ,'category/treatment.html' )

def water(request):
    return render(request ,'category/water.html' )

def orphans(request):
    return render(request ,'category/yatem.html' )

def orphans_marriage(request):
    return render(request ,'category/yatemat.html' )
    
def fetr(request):
    return render(request ,'category/fetr.html' )

def gold_zakat(request):
    return render(request ,'category/gold_zakat.html' )

def land(request):
    return render(request ,'category/land.html' )

def Money_zakat(request):
    return render(request ,'category/Money_zakat.html' )

def out_of_land(request):
    return render(request ,'category/out-of-land.html' )

def rekaz(request):
    return render(request ,'category/rekaz.html' )

def silver_zakat(request):
    return render(request ,'category/silver_zakat.html' )

def trade(request):
    return render(request ,'category/trade.html' )

'''
def category_detail(request,id):
    category_detail = Category.objects.get(id=id)
    context = {'category_detail' : category_detail}
    return render ( request , 'Category/zakat.html' , context)
    '''