from django.db import models
from category.models import Subcategory
                                                 #importing

class Old_people(models.Model):
    id = models.BigAutoField(primary_key=True)
    family_member = models.CharField(max_length=255)
    income = models.CharField(max_length=255)
    have_disease = models.CharField(max_length=255)
    have_assets = models.CharField(max_length=255)
    require_special_care = models.CharField(max_length=255) 
                                                 #database 
class Orphan_support(models.Model):
    id = models.BigAutoField(primary_key=True)
    age = models.CharField(max_length=255)
    have_family = models.CharField(max_length=255)
    income = models.CharField(max_length=255)
    have_special_need = models.CharField(max_length=255)
                                                 #database 

class Debtors(models.Model):
    id = models.BigAutoField(primary_key=True)
    income = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    amount_of_debt = models.CharField(max_length=255)
    remaining_time = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
                                                 #database 

class Clothes(models.Model):
    id = models.BigAutoField(primary_key=True)
    age = models.CharField(max_length=255)
    family_member = models.CharField(max_length=255)
    family_member_who_able_to_work = models.CharField(max_length=255)
    income = models.CharField(max_length=255)
    there_is_children = models.CharField(max_length=255)  
                                                 #database 

class Food_support(models.Model):
    id = models.BigAutoField(primary_key=True)
    age = models.CharField(max_length=255)
    family_member = models.CharField(max_length=255)
    family_member_who_able_to_work = models.CharField(max_length=255)
    income = models.CharField(max_length=255)
    there_is_children = models.CharField(max_length=255)      
                                                 #database 

class House_improvement(models.Model):
    id = models.BigAutoField(primary_key=True)
    important = models.CharField(max_length=255)
    isolated_city = models.CharField(max_length=255)
    count = models.CharField(max_length=255)
    type_of_development = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
                                                 #database 

class Surgery(models.Model):
    id = models.BigAutoField(primary_key=True)
    age = models.CharField(max_length=255)
    time_pending = models.CharField(max_length=255)
    critical = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    success_ratio = models.CharField(max_length=255)
    can_work_after = models.CharField(max_length=255)
                                                 #database 

class Heart_surgery(models.Model):
    id = models.BigAutoField(primary_key=True)
    age = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    time_pending = models.CharField(max_length=255)
    remaning_time = models.CharField(max_length=255)
    need_to_travel = models.CharField(max_length=255) 
    need_transplant = models.CharField(max_length=255)    
                                                 #database 

class Treatment(models.Model):
    id = models.BigAutoField(primary_key=True)
    age = models.CharField(max_length=255)
    treatment_type = models.CharField(max_length=255)
    critical = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
                                                 #database 

class Special_abilities(models.Model):
    id = models.BigAutoField(primary_key=True)
    age = models.CharField(max_length=255)
    time_pending = models.CharField(max_length=255)
    vitality = models.CharField(max_length=255)
    critical = models.CharField(max_length=255)
    need_to_travel = models.CharField(max_length=255) 
    require_special_care = models.CharField(max_length=255) 
    can_work_before = models.CharField(max_length=255)
                                                 #database 

class Tumor(models.Model):
    id = models.BigAutoField(primary_key=True)
    age = models.CharField(max_length=255)
    phase = models.CharField(max_length=255)
    critical = models.CharField(max_length=255)
    criticality_of_place = models.CharField(max_length=255)
    time_pending = models.CharField(max_length=255) 
    remaining_time = models.CharField(max_length=255)         
                                                 #database 

class Accident_burns(models.Model):
    id = models.BigAutoField(primary_key=True)
    tyoe_of_burn = models.CharField(max_length=255)
    critical = models.CharField(max_length=255)
    income = models.CharField(max_length=255)
    can_work_after = models.CharField(max_length=255)
    time_pending = models.CharField(max_length=255) 
    plastic_surgery = models.CharField(max_length=255) 
                                                 #database 

class Habilitation(models.Model):
    id = models.BigAutoField(primary_key=True)
    age = models.CharField(max_length=255)
    amount = models.CharField(max_length=255)
    fesability_and_ability_to_manage = models.CharField(max_length=255)
    income = models.CharField(max_length=255)
    family_member = models.CharField(max_length=255) 
                                                 #database 

Feature = (
    ('Old_people',Old_people),
    ('Orphan_support',Orphan_support),
    ('Debtors',Debtors),
    ('Clothes',Clothes),
    ('Food_support',Food_support),
    ('House_improvement',House_improvement),
    ('Surgery',Surgery),
    ('Heart_surgery',Heart_surgery),
    ('Treatment',Treatment),
    ('Special_abilities',Special_abilities),
    ('Tumor',Tumor),
    ('Accident_burns',Accident_burns),
    ('Habilitation',Habilitation),
   ) 
                                                 #choices_of_superfeatures 

class Features(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255,choices=Feature, null=True , verbose_name=("Subcategory Feature"))
    sub = models.ForeignKey(Subcategory, on_delete=models.CASCADE , null=True ,verbose_name=("Subcategory Name"))
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


