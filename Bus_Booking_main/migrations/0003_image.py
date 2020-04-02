# Generated by Django 2.2.10 on 2020-04-02 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Bus_Booking_main', '0002_auto_20200330_2009'),
    ]

    operations = [
        migrations.CreateModel(
            name='image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images_upload', models.ImageField(default='', upload_to='busbooking/images')),
                ('busbooking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BusBooking', to='Bus_Booking_main.BusBooking')),
            ],
        ),
    ]