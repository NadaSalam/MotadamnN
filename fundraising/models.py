from django.db import models
from subcategory.models import Subcategory
                                                     #importing

class Fundraising(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    photo = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    sub = models.ForeignKey(Subcategory, models.DO_NOTHING)
                                                     #database
    def __str__(self):
        return self.name
                                                     #to retrive the object name                                                 

    class Meta:
        managed = True
        db_table = 'fundraising'
                                                     #managing by
