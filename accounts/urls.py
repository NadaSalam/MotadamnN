
from django.urls import path
from . import views

urlpatterns = [
    path('accounts/sign_in',views.sign_in),

]
