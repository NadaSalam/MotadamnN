from django.contrib import admin
from .models import Category , Subcategory
                                                 #importing

admin.site.register(Subcategory)
admin.site.register(Category)
                                                 #to view in admin

