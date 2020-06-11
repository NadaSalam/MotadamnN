from django.db import models
from cases.models import Cases  
from features.models import Features
                                                 #importing

class Cases_Features(models.Model):
    id = models.BigAutoField(primary_key=True)
    cases = models.ForeignKey(Cases, models.DO_NOTHING)
    features = models.ForeignKey(Features , models.DO_NOTHING)
    answer = models.CharField(max_length=255)
                                                 #database
    class Meta:
        verbose_name = 'Cases Features'
        verbose_name_plural = 'Cases Features'
                                                 #to rename the plural name in admin
        managed = True
        db_table = 'cases_features'
                                                 #managing by
