from django.urls import path
from . import views

app_name='donation'

urlpatterns = [
    
        path('donation/',views.donation , name='donation'),

    ]
