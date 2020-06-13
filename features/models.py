from django.db import models
from category.models import Subcategory

                                                 #importing

Feature = (
    ('have family','have family'),
    ('zakat','zakat'),
    ('health','health'),
    ('economic','economic'),
    ('improvement','improvement'),
   )
                                                  #choices of features  
old_people = ( 
    ('have family','have family'),
    ('zakat','zakat'),
    ('health','health'),
    ('economic','economic'),
    ('improvement','improvement'),
   )                                    
                                                  #choices of old_people program  

class Features(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name=("Feature Name"))
    subcat = models.ManyToManyField(Subcategory)
                                                 #database
    def __str__(self):
        return self.name
                                                 #to retrive the object name

    class Meta:
        verbose_name = 'features'
        verbose_name_plural = 'features' 
                                                 #to rename the plural name in admin
        managed = True
        db_table = 'features'
                                                  #managing by

