from django.contrib import admin
from category.models import Category
from category.models import Subcategory
                                                 #importing

admin.site.register(Subcategory)
admin.site.register(Category)
                                                 #to view in admin

