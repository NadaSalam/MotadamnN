
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('all_cases', views.all_cases),
    path('about_us', views.about_us),
    path('contact_us', views.contact_us),
    path('news', views.news),
    path('question_answer', views.question_answer),

    path('', include('category.urls')),
    path('', include('donation.urls')),
    path('', include('features.urls')),
    path('', include('donor.urls')),
    path('', include('cases.urls')),
    path('', include('charity.urls')),
    path('', include('beneficiary.urls')),
    path('', include('accounts.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
