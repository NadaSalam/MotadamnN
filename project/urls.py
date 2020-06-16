
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home , name='home'),
    path('pay/', views.pay , name='pay'),
    path('finish/', views.finish , name='finish'),
    path('all_cases/', views.all_cases , name='all_cases'),
    #path('category/', include('category.urls' , namespace='category')),
    path('donation/', include('donation.urls', namespace='donations')),

    path('', include('features.urls')),
    path('', include('donor.urls')),
    path('', include('cases.urls')),
    path('', include('charity.urls')),
    path('', include('beneficiary.urls')),
    path('', include('accounts.urls')),
    path('', include('category.urls')),


    path('about_us/', views.about_us , name='about_us'),
    path('contact_us/', views.contact_us , name='contact_us'),
    path('news/', views.news , name='news'),
    path('question_answer/', views.question_answer , name='question_answer'  ),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
