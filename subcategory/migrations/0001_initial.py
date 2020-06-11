# Generated by Django 3.0.7 on 2020-06-09 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('supercategory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('super', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supercategory.Supercategory')),
            ],
            options={
                'verbose_name': 'Subcategory',
                'verbose_name_plural': 'Subcategories',
                'db_table': 'subcategory',
                'managed': True,
            },
        ),
    ]