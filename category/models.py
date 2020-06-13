from django.db import models
                                                  #importing
Supercat = (
    ('social_support','social_support'),
    ('zakat','zakat'),
    ('health','health'),
    ('economic','economic'),
    ('improvement','improvement'),
   )
                                                  #choices of supercategory 
Subcat = (
    ('old_people','old_people'),
    ('poor','poor'),
    ('health','health'),
    ('economic','economic'),
    ('improvement','improvement'),
   )                                               
                                                     #choices of subcategory 
  
class Category(models.Model):
   id = models.BigAutoField(primary_key=True)                                              
   name = models.CharField(max_length=255,choices=Supercat, verbose_name=("Supercategory Name"))
                                                 #database
   def __str__(self):
        return self.name
                                                 #to retrive the object name
   class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
                                                 #to rename the plural name in admin
class Subcategory(models.Model):
    
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255,choices=Subcat, verbose_name=("Subcategory Name"))
    parent = models.ForeignKey(Category,on_delete=models.CASCADE, verbose_name=("Subcategory Name") ) 
                                                 #database

    def __str__(self):
        return self.name
                                                 #to retrive the object name

    class Meta:
        verbose_name = 'subcategory'
        verbose_name_plural = 'subcategories'
                                                 #to rename the plural name in admin

        managed = True
        db_table = 'category'
                                                 #managing by
       
