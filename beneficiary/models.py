from django.db import models
from charity.models import Charity
import datetime


class Beneficiary(models.Model):
    id = models.BigAutoField(primary_key=True)
    national_id = models.BigIntegerField(unique=True)
    gender = models.IntegerField()
    martial_status = models.CharField(max_length=8, verbose_name="beneficiary status")
    name = models.CharField(max_length=255 ,verbose_name="beneficiary name" )
    address = models.CharField(max_length=255, verbose_name="beneficiary address")
    city = models.CharField(max_length=255)
    birthdate = models.DateField()
    photo  = models.ImageField(upload_to='beneficiary/')
    created_at = models.DateTimeField(blank=True, default=datetime.datetime.now)
    charity = models.ForeignKey(Charity,on_delete=models.PROTECT)
    def __str__(self):
        return self.name

#ooo
    class Meta:
        verbose_name = 'beneficiary'
        verbose_name_plural = 'beneficiaries'
        managed = True
        db_table = 'beneficiary'
