from django.db import models
import datetime
from django.utils import timezone
                                                     #importing

class Charity(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name=("Charity Name"))
    email = models.CharField(unique=True, max_length=255, verbose_name=("Charity Email"))
    phone = models.CharField(max_length=255, verbose_name=("Charity Phone Number"))
    address = models.CharField(max_length=255, verbose_name=("Charity Address"))
    logo  = models.ImageField(upload_to='charity/', verbose_name=("Charity Logo"))
    description = models.TextField(verbose_name=("Charity Description"))
    password = models.CharField(max_length=255, verbose_name=("Charity Password"))
    is_banned = models.BooleanField(default=False, verbose_name=("Banned! " ))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=("Time of Creation"))
    city = models.CharField(max_length=255, verbose_name=("Charity City"))
                                                     #database

    def __str__(self):
        return self.name
                                                     #to retrive the object name

    class Meta:
        verbose_name = 'charity'
        verbose_name_plural = 'charities'
                                                     #to rename the plural name in admin
           
        managed = True
        db_table = 'charity'
                                                     #managing by
