
from django.db import models
from django.utils.translation import ugettext_lazy as _
from multiselectfield import MultiSelectField
from django.utils.html import escape
from django.utils.html import mark_safe
Select_Facilitiesy = (
    ('WIFI', 'WIFI'),
    ('Food', 'Food'),
    
)

Select_Service_Range = (
    ('India', 'India'),
    ('International', 'International'),

)
Select_City = (
    ('mumbai', 'Mumbai'),
    ('delhi', 'Delhi'),
    ('Bangalore', 'Bangalore'),
    ('Hyderabad', 'Hyderabad'),
    ('Ahmedabad', 'Ahmedabad'),
)

INACTIVE = 0
ACTIVE = 1
STATUS = (
    (INACTIVE, _('Inactive')),
    (ACTIVE, _('Active')),
)
DAY_OF_THE_WEEK = (
        ('Monday','Monday'),
        ('Tuesday','Tuesday'),
        ('Wednesday','Wednesday'),
        ('Thursday','Thursday'),
        ('Friday','Friday'),
        ('Saturday','Saturday'),
        ('Sunday','Sunday'),
    )
Select_Rating = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)
Select_Bus_Type  = (
    ('Non AC Seater ', 'Non AC Seater '),
    ('Non AC Sleeper', 'Non AC Sleeper'),
    ('AC Seater', 'AC Seater'),
    ('AC Sleeper', 'AC Sleeper'),

)
TIME_CHOICES = (('00:00:00', 'Midnight'),
                    ('01:00:00', '01 AM'),
                    ('02:00:00', '02 AM'),
                    ('03:00:00', '03 AM'),
                    ('04:00:00', '04 AM'),
                    ('05:00:00', '05 AM'),
                    ('06:00:00', '06 AM'),
                    ('07:00:00', '07 AM'),
                    ('08:00:00', '08 AM'),
                    ('09:00:00', '09 AM'),
                    ('10:00:00', '10 AM'),
                    ('11:00:00', '11 AM'),
                    ('12:00:00', 'Noon'),
                    ('13:00:00', '01 PM'),
                    ('14:00:00', '02 PM'),
                    ('15:00:00', '03 PM'),
                    ('16:00:00', '04 PM'),
                    ('17:00:00', '05 PM'),
                    ('18:00:00', '06 PM'),
                    ('19:00:00', '07 PM'),
                    ('20:00:00', '08 PM'),
                    ('21:00:00', '09 PM'),
                    ('22:00:00', '10 PM'),
                    ('23:00:00', '11 PM'), 
)
# Create your models here.


class BusBooking(models.Model):
    Name_of_Bus = models.CharField(max_length=100)
    From_City = models.CharField(max_length=200, choices=Select_City)
    To_City = models.CharField(max_length=200, choices=Select_City)
    Bus_Type=models.CharField(max_length=200, choices=Select_Bus_Type)
    Facilities = MultiSelectField(choices=Select_Facilitiesy)
    Service_Range = models.CharField(
        max_length=10, choices=Select_Service_Range)
    Days_of_Operations = models.CharField(
        max_length=200, choices=DAY_OF_THE_WEEK)
    Depature_Time = models.TimeField()
    Arrival_Time = models.TimeField()
    Rating = models.CharField(max_length=200, choices=Select_Rating)
    Ticket_Amount_Per_Passenger=models.CharField(max_length=100)
    Brief_Over_Facilities = models.TextField(max_length=500)
    Travel_Agency=models.CharField(max_length=100)
    Status = models.IntegerField(default=0, choices=STATUS)
    AddedOn = models.DateField()
class image(models.Model):
    busbooking=models.ForeignKey(BusBooking, on_delete=models.CASCADE, related_name='BusBooking')
    images_upload = models.ImageField(upload_to='busbooking/images',default="")
