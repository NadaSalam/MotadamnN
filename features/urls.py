from django.urls import path
from . import views

urlpatterns = [
    path('features/aoram/',views.aoram , name='aoram'),
    path('features/burns/',views.burns , name='burns'),
    path('features/clothes/',views.clothes , name='clothes'),
    path('features/development/',views.development , name='development'),
    path('features/economic/',views.economic , name='economic'),
    path('features/gharmeen/',views.gharmeen , name='gharmeen'),
    path('features/heart/',views.heart , name='heart'),
    path('features/mosneen/',views.mosneen , name='mosneen'),
    path('features/special_people/',views.special_people , name='special_people'),
    path('features/surgery/',views.surgery , name='surgery'),
    path('features/treatment/',views.treatment , name='treatment'),
    path('features/yeatem/',views.yeatem , name='yeatem'),
]
