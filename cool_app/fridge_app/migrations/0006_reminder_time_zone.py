# Generated by Django 3.2.20 on 2023-08-16 18:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fridge_app', '0005_reminder'),
    ]

    operations = [
        migrations.AddField(
            model_name='reminder',
            name='time_zone',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
