# Generated by Django 2.2.12 on 2022-06-15 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booktable',
            name='bdate',
            field=models.DateField(verbose_name='Booking Date'),
        ),
    ]
