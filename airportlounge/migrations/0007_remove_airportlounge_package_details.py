# Generated by Django 2.2.10 on 2020-03-24 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('airportlounge', '0006_packagedetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='airportlounge',
            name='Package_Details',
        ),
    ]
