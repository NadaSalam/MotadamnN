from django.db import models
from subcategory.models import Subcategory
from features.models import Features


class SubcategoryFeatures(models.Model):
    id = models.BigAutoField(primary_key=True)
    subcat = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    feature = models.ForeignKey(Features, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'SubcategoryFeature'
        verbose_name_plural = 'SubcategoryFeatures'
        managed = True
        db_table = 'subcategory_features'
