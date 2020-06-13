from django.db import models
from category.models import Subcategory


                                             #importing
Feature = (
    ('have family','have family'),
    ('income','income'),
    ('have_disease','have_disease'),
    ('have_assets','have_assets'),
    ('require_special_care','require_special_care'),
    ('age','age'),
    ('amount_of_debt','amount_of_debt'),
    ('remaning_time','remaning_time'),
    ('gender','gender'),
    ('amount','amount'),
    ('fesability_and_ability_to_manage','fesability_and_ability_to_manage'),
    ('type_of_burn','type_of_burn'),
    ('critical','critical'),
    ('can_work_after','can_work_after'),
    ('time_pending','time_pending'),
    ('plastic_surgery','plastic_surgery'),
    ('vitality','vitality'),
    ('can_work_before','can_work_before'),
    ('need_to_travel','need_to_travel'),
    ('status','status'),
    ('success_ratio','success_ratio'),
    ('important','important'),
    ('isolated_city','isolated_city'),
    ('count','count'),
    ('type_of_development','type_of_development'),
    ('number','number'),
    ('have_special_need','have_special_need'),
    ('there’s_children','there’s_children'),
    ('need_transplant','need_transplant'),
    ('phase','phase'),
    ('criticality_of_place','criticality_of_place'),
    ('treatment_type','treatment_type'),
    ('Family_member','Family_member'),
    ('family_member_who_able_work','family_member_who_able_work'),
   )
                                                  #choices of features
old_people = (
        ('Family_member','Family_member'),
        ('income','income'),
        ('have_disease','have_disease'),
        ('have_assets','have_assets'),
        ('require_special_care','require_special_care'),
  )
                                                        #choices of old_people program

orphan_support =(
      ('age','age'),
      ('have family','have family'),
      ('income','income'),
      ('have_special_need','have_special_need'),
  )
                                                        #choices of orphan_support program

debtors =(
      ('income','income'),
      ('age','age'),
      ('amount_of_debt','amount_of_debt'),
      ('remaning_time','remaning_time'),
      ('gender','gender'),
  )
                                                         #choices of debtors program

clothes =(
    ('age','age'),
    ('Family_member','Family_member'),
    ('family_member_who_able_work','family_member_who_able_work'),
    ('income','income'),
    ('there’s_children','there’s_children'),
    ('criticality_of_place','criticality_of_place'),
  )
                                                         #choices of clothes program

food_support =(
      ('age','age'),
      ('Family_member','Family_member'),
      ('family_member_who_able_work','family_member_who_able_work'),
      ('income','income'),
      ('there’s_children','there’s_children'),
      ('criticality_of_place','criticality_of_place'),
  )
                                                          #choices of food_support program

house_improvement =(
        ('important','important'),
        ('isolated_city','isolated_city'),
        ('count','count'),
        ('type_of_development','type_of_development'),
        ('number','number'),
  )
                                                        #choices of house_improvement program

surgery =(
      ('age','age'),
      ('time_pending','time_pending'),
      ('critical','critical'),
      ('status','status'),
      ('success_ratio','success_ratio'),
      ('can_work_after','can_work_after'),

  )
                                                         #choices of surgery program

heart_surgery = (
        ('age','age'),
        ('status','status'),
        ('time_pending','time_pending'),
        ('remaning_time','remaning_time'),
        ('need_to_travel','need_to_travel'),
        ('need_transplant','need_transplant'),
  )
                                                        #choices of heart_surgery program

treatment =(
        ('age','age'),
        ('treatment_type','treatment_type'),
        ('critical','critical'),
        ('status','status'),
  )
                                                      #choices of treatment program

special_abilities = (
        ('age','age'),
        ('time_pending','time_pending'),
        ('vitality','vitality'),
        ('critical','critical'),
        ('need_to_travel','need_to_travel'),
        ('require_special_care','require_special_care'),
        ('can_work_before','can_work_before'),
  )
                                                     #choices of special_abilities program

tumor = (
    ('age','age'),
    ('phase','phase'),
    ('critical','critical'),
    ('criticality_of_place','criticality_of_place'),
    ('time_pending','time_pending'),
    ('remaning_time','remaning_time'),
  )
                                                      #choices of tumor program
accident_burns =(
       ('type_of_burn','type_of_burn'),
       ('critical','critical'),
       ('income','income'),
       ('can_work_after','can_work_after'),
       ('time_pending','time_pending'),
       ('plastic_surgery','plastic_surgery'),
  )
                                                 #choices of accident_burns program

habilitation =(
       ('age','age'),
       ('amount','amount'),
       ('fesability_and_ability_to_manage','fesability_and_ability_to_manage'),
       ('income','income'),
       ('Family_member','Family_member'),
  )
                                                #choices habilitation program
charity_project =(
             ('age','age'),
             ('amount','amount'),
             ('fesability_and_ability_to_manage','fesability_and_ability_to_manage'),
             ('income','income'),
             ('Family_member','Family_member'),
  )
                                                 #choices charity_project program

cattle_distribution =(
             ('age','age'),
             ('amount','amount'),
             ('fesability_and_ability_to_manage','fesability_and_ability_to_manage'),
             ('income','income'),
             ('Family_member','Family_member'),
  )
                                                #choices cattle_distribution program

good_loan =(
        ('age','age'),
        ('amount','amount'),
        ('fesability_and_ability_to_manage','fesability_and_ability_to_manage'),
        ('income','income'),
        ('Family_member','Family_member'),
  )
                                                #choices good_loan program


class Features(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name=("Feature Name"))
    subcat = models.ManyToManyField(Subcategory)
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
