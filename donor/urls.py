from django.urls import path
from . import views

urlpatterns = [
    path('donor/profile',views.profile),

]
