# Generated by Django 3.0.7 on 2020-06-12 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supercategory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supercategory',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Category Name'),
        ),
    ]
