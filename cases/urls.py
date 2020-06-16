from django.urls import path
from . import views

urlpatterns = [
    path('cases/card/',views.card , name='card' ),
    path('cases/without_img/',views.without_img  , name='without_img'),
    path('cases/without_img1/',views.without_img1 , name='without_img1'),

]
