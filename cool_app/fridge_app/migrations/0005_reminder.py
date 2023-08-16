# Generated by Django 3.2.20 on 2023-08-16 17:57

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fridge_app', '0004_alter_receipt_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('D', 'Day'), ('E', 'Expiration'), ('G', 'Garbage')], default='D', max_length=1)),
                ('date', models.DateTimeField(verbose_name='Reminder Date')),
                ('Day(s) Prio', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(6)])),
                ('remind_time', models.CharField(choices=[('M', 'Morning'), ('L', 'Noon'), ('A', 'Afternoon'), ('E', 'Evening'), ('N', 'Night')], default='M', max_length=1)),
                ('send_to_email', models.EmailField(max_length=70)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]
