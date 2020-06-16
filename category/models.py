from django.db import models
                                                 #importing
Supercat = (
    ('social_support','social_support'),
    ('zakat','zakat'),
    ('health','health'),
    ('economic','economic'),
    ('improvement','improvement'),
   )
                                                  #choices of supercategory 
Subcat = (
    ('old_people','old_people'),
    ('orphan_support','orphan_support'),
    ('debtors','debtors'),
    ('orphan_marriage','orphan_marriage'),
    ('clothes','clothes'),
    ('blind','blind'),
    ('street_children','street_children'),
    ('food_support ','food_support '),
    ('eighth_zakat ','eighth_zakat '),
    ('trade_zakat','trade_zakat'),
    ('elfitr_zakat ','elfitr_zakat '),
    ('debts_zakat ',' debts_zakat '),
    ('animal_zakat ','animal_zakat '),
    ('plant_zakat ','plant_zakat '),
    ('crop_zakat ','crop_zakat '),
    ('land_zakat ','land_zakat '),
    ('ore_zakat ','ore_zakat '),
    ('water_purification ','water_purification '),
    ('water_meter ','water_meter '),
    ('house_improvement ','house_improvement '),
    ('surgery ','surgery '),
    ('medical_test ','medical_test '),
    ('addiction_treatment ','artificial_limbs '),
    ('artificial_limbs','artificial_limbs'),
    ('kidney_dialysis','kidney_dialysis'),
    ('deaf_speechless ','deaf_speechless '),
    ('heart_surgery','heart_surgery'),
    ('treatment ','treatment '),
    ('special_abilities ','special_abilities '),
    ('tumor ','tumor '),
    ('virus_c ','virus_c '),
    ('baby_nurseries ','baby_nurseries '),
    ('animal_welfare ','animal_welfare '),
    ('accident_burns ','accident_burns '),
    ('breast_cancer ','breast_cancer '),
    ('habilitation ','habilitation '),
    ('charity_project ','charity_project '),
    ('cattle_distribution ','cattle_distribution '),
    ('good_loan ','good_loan '),
   )                                               
                                                     #choices of subcategory 
  
class Category(models.Model):
   id = models.BigAutoField(primary_key=True)                                              
   name = models.CharField(max_length=255,choices=Supercat, verbose_name=("Supercategory Name"))
                                                 #database
   def __str__(self):
        return self.name
                                                 #to retrive the object name
   class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
                                                 #to rename the plural name in admin
class Subcategory(models.Model):
    
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255,choices=Subcat, verbose_name=("Subcategory Name"))
    parent = models.ForeignKey(Category,on_delete=models.CASCADE, verbose_name=("Supercategory Name") ) 
                                                 #database

    def __str__(self):
        return self.name
                                                 #to retrive the object name

    class Meta:
        verbose_name = 'subcategory'
        verbose_name_plural = 'subcategories'
                                                 #to rename the plural name in admin

        managed = True
        db_table = 'category'
                                                 #managing by
       
