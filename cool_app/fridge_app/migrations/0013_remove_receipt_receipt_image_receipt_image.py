# Generated by Django 4.2.4 on 2023-08-16 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fridge_app', '0012_merge_20230816_2205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receipt',
            name='receipt_image',
        ),
        migrations.AddField(
            model_name='receipt',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]