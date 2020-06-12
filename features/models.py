from django.db import models

                                                 #importing
class Features(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name=("Feature Name"))
                                                 #database
    def __str__(self):
        return self.name
                                                 #to retrive the object name
    class Meta:
        verbose_name = 'features'
        verbose_name_plural = 'features'
                                                 #to rename the plural name in admin
        managed = True
        db_table = 'features'
                                                  #managing by
