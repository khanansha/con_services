# Generated by Django 2.2.10 on 2020-03-24 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('airportlounge', '0002_auto_20200323_1837'),
    ]

    operations = [
        migrations.CreateModel(
            name='AirportLounge_images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(default='', upload_to='airportlounge/images')),
                ('airportlounge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='airportlounge', to='airportlounge.AirportLounge')),
            ],
        ),
    ]