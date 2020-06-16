from django.db import models
from charity.models import Charity
import datetime
from django.utils import timezone
                                                     #importing

class Beneficiary(models.Model):
    id = models.BigAutoField(primary_key=True)
    national_id = models.BigIntegerField(unique=True)
    gender = models.IntegerField()
    martial_status = models.CharField(max_length=8, verbose_name="beneficiary status")
    name = models.CharField(max_length=255 ,verbose_name="beneficiary name" )
    address = models.CharField(max_length=255, verbose_name="beneficiary address")
    city = models.CharField(max_length=255)
    birthdate = models.DateField()
    photo = models.ImageField(upload_to='beneficiary/', null=True)
    phone = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    charity = models.ForeignKey(Charity,on_delete=models.PROTECT)
                                                     #database

    def __str__(self):
        return self.name
                                                     #to retrive the object name

    class Meta:
        verbose_name = 'beneficiary'
        verbose_name_plural = 'beneficiaries'
                                                             #to rename the plural name in admin

        managed = True
        db_table = 'beneficiary'
                                                     #managing by
