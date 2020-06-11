from django.db import models
from donation.models import Donation
from cases.models import Cases
                                                     #importing

class DonationCases(models.Model):
    id = models.BigAutoField(primary_key=True)
    donation = models.ForeignKey(Donation, models.DO_NOTHING)
    cases = models.ForeignKey(Cases, models.DO_NOTHING)
                                                     #database

    class Meta:
          verbose_name = 'Donation Cases'
          verbose_name_plural = 'Donation Cases'
                                                     #to rename the plural name in admin
          managed = True
          db_table = 'donation_cases'
                                                     #managing by                                           
