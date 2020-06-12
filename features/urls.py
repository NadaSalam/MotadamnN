from django.urls import path
from . import views

urlpatterns = [
    path('features/aoram',views.aoram),
    path('features/burns',views.burns),
    path('features/clothes',views.clothes),
    path('features/development',views.development),
    path('features/economic',views.economic),
    path('features/gharmeen',views.gharmeen),
    path('features/heart',views.heart),
    path('features/mosneen',views.mosneen),
    path('features/special_people',views.special_people),
    path('features/surgery',views.surgery),
    path('features/treatment',views.treatment),
    path('features/yeatem',views.yeatem),
]
