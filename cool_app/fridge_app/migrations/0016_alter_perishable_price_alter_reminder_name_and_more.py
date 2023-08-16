# Generated by Django 4.2.4 on 2023-08-16 23:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fridge_app', '0015_merge_20230816_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perishable',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Total'),
        ),
        migrations.AlterField(
            model_name='reminder',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='reminder',
            name='remind_days_prio_by',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(6)]),
        ),
    ]