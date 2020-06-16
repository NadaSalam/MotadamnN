from django.db import models
from donor.models import Donor
from cases.models import Cases
import datetime
from django.utils import timezone
                                                     #importing

class Donation(models.Model):
    id = models.BigAutoField(primary_key=True)
    donation_ref = models.CharField(unique=True, max_length=255)
    payment_amount = models.IntegerField()
    payment_method = models.CharField(max_length=7)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    donor = models.ForeignKey(Donor,on_delete=models.PROTECT)
    case = models.ManyToManyField(Cases)
    
                                                     #database

    class Meta:    
        managed = True
        db_table = 'donation'
                                                     #managing by
