from django.db import models
from supercategory.models import Supercategory

class Subcategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    super = models.ForeignKey(Supercategory, on_delete=models.CASCADE )
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Subcategory'
        verbose_name_plural = 'Subcategories'
        managed = True
        db_table = 'subcategory'
