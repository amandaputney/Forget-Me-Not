# Generated by Django 4.2.4 on 2023-08-23 15:03

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField(blank=True, max_length=300)),
                ('date', models.DateField()),
                ('time', models.TimeField(default='06:00')),
                ('send_to_email', models.EmailField(max_length=70)),
                ('task_id', models.CharField(max_length=200, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=30)),
                ('purchase_date', models.DateField(verbose_name='Purchase Date')),
                ('receipt_total', models.DecimalField(decimal_places=2, default=0, max_digits=8, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Total')),
                ('item_list', models.TextField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('url', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-purchase_date'],
            },
        ),
        migrations.CreateModel(
            name='Perishable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('quantity', models.DecimalField(decimal_places=0, default=1, max_digits=3, validators=[django.core.validators.MinValueValidator(1)])),
                ('store_name', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('B', 'Bakery 🍞'), ('D', 'Dairy 🥛'), ('E', 'Eggs 🐔'), ('M', 'Meat and Seafood 🍖'), ('P', 'Produce 🥦'), ('O', 'Other 🍕')], max_length=1)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Price')),
                ('expiration', models.DateField(verbose_name='Expiration Date')),
                ('receipt', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fridge_app.receipt')),
                ('reminders', models.ManyToManyField(to='fridge_app.reminder')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
