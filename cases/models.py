from django.db import models
from beneficiary.models import Beneficiary
from category.models import Subcategory
import datetime
from django.utils import timezone
                                                     #importing
class Cases(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.TextField()
    needed_amount = models.IntegerField()
    approved = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    sub = models.ForeignKey(Subcategory, on_delete=models.PROTECT,null=True)
    ben = models.ForeignKey(Beneficiary, on_delete=models.PROTECT,null=True)
                                                     #database

    def __str__(self):
        return '%s' %(self.ben)
                                                     #to retrive the object name

    class Meta:
        verbose_name = 'case'
        verbose_name_plural = 'cases'
                                                             #to rename the plural name in admin                                                                   #to rename the plural name in admin

        managed = True
        db_table = 'cases'
                                                             #managing by

