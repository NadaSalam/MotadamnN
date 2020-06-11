from django.db import models
from donor.models import Donor
                                                     #importing

class Donation(models.Model):
    id = models.BigAutoField(primary_key=True)
    donation_ref = models.CharField(unique=True, max_length=255)
    payment_amount = models.IntegerField()
    payment_method = models.CharField(max_length=7)
    created_at = models.DateTimeField()
    donor = models.ForeignKey(Donor, models.DO_NOTHING)
                                                     #database

    class Meta:    
        managed = True
        db_table = 'donation'
                                                     #managing by
