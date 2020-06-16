from django.urls import path
from . import views

urlpatterns = [
    path('beneficiary/without_img/',views.without_img , name='without_img' ),
    path('beneficiary/with_img/',views.with_img , name='with_img' ),


]
