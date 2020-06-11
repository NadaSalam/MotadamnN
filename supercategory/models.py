from django.db import models
                                                 #importing

class Supercategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name=("Category Name"))
                                                 #database

    def __str__(self):
        return self.name
                                                 #to retrive the object name

    class Meta:
        verbose_name = 'supercategory'
        verbose_name_plural = 'supercategories'
                                                 #to rename the plural name in admin

        managed = True
        db_table = 'supercategory'
                                                 #managing by
       
