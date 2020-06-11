from django.db import models

                                                     #importing
class Donor(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name=("Donor Name"))
    phone = models.CharField(max_length=255, verbose_name=("Donor Phone Number"))
    address = models.CharField(max_length=255, verbose_name=("Donor Address"))
    email = models.CharField(unique=True, max_length=255, verbose_name=("Donor Email"))
    gender = models.IntegerField(verbose_name=("Donor Gender"))
    birthdate = models.DateField(verbose_name=("Donor Birthdate"))
    username = models.CharField(max_length=255, verbose_name=("Donor Username"))
    password = models.CharField(max_length=255, verbose_name=("Donor Password"))
    is_banned = models.IntegerField( verbose_name=("Banned!"))
    created_at = models.DateTimeField( verbose_name=("Donor Name"))
                                                     #database for donor
    def __str__(self):
        return self.name
                                                     #to retrive the object name
    class Meta:
        managed = True
        db_table = 'donor'
                                                     #managing by  
                                                     
