from django.urls import path
from . import views

urlpatterns = [
    path('charity/game3_mostafeden',views.game3_mostafeden),
    path('charity/gme3halatwaiting',views.gme3halatwaiting),
    path('charity/halataccepted',views.halataccepted),
    path('charity/profile_elgm3ia',views.profile_elgm3ia),
    path('charity/add_mostafed',views.add_mostafed),

]
