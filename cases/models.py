from django.db import models
from beneficiary.models import Beneficiary
from subcategory.models import Subcategory

class Cases(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.TextField()
    needed_amount = models.IntegerField()
    approved = models.IntegerField()
    subcat = models.ForeignKey(Subcategory, on_delete=models.CASCADE , null=True)
    ben = models.ForeignKey(Beneficiary, on_delete=models.DO_NOTHING)
    def __str__(self):
        return '%s' %(self.ben)

    class Meta:
        verbose_name = 'case'
        verbose_name_plural = 'cases'
        managed = True
        db_table = 'cases'
