# Generated by Django 2.2.10 on 2020-03-24 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airportlounge', '0004_auto_20200324_1407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='airportlounge_images',
            name='Package_Details',
        ),
        migrations.AddField(
            model_name='airportlounge',
            name='Package_Details',
            field=models.TextField(default='', max_length=100),
        ),
    ]
