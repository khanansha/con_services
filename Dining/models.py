
# Create your models here.

from django.db import models
from django.utils.html import escape
from django.utils.html import mark_safe
#from django_countries.fields import CountryField
#from django_countries.countries import COUNTRIES
#from localflavor.us.us_states import STATE_CHOICES
#from localflavor.us.models import USStateField
#from django.contrib.localflavor.us.us_states import STATE_CHOICES




# Create your models here.
Select_Category = (
    ('famous','Famous'),
    ('trending in city', 'Trending in city'),
    ('happeing Nightlife','Happeing Nightlife'),
)
Select_Rating=(
    ('1','1'),
    ('2', '2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
)

Select_City=(
    ('mumbai','Mumbai'),
    ('delhi', 'Delhi'),
    ('Bangalore','Bangalore'),
    ('Hyderabad','Hyderabad'),
    ('Ahmedabad','Ahmedabad'),
)

Select_Area=(
    ('andheri','Aandheri'),
    ('malad', 'Malad'),
    ('marol','Marol'),
    ('chembure','Chembure'),
    ('vashi','Vashi'),
)

Select_State=(
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Assam ', 'Assam'),
    ('Bihar ','Bihar'),
    ('Goa','Goa'),
    ('Gujarat','Gujarat'),
    ('Maharashtra','Maharashtra'),
)
#Select_Country=(
 #   ('Argentina','Argentina'),
  #  ('Angola ', 'Angola'),
   # ('America ','America'),
    #('England','England'),
    #('India','India'),
#)
Select_Country=(
    ('AD', 'Andorra'),
    ('AE', 'United Arab Emirates'),
    ('AF', 'Afghanistan'),
    ('AG', 'Antigua & Barbuda'),
    ('AI', 'Anguilla'),
    ('AL', 'Albania'),
    ('AM', 'Armenia'),
    ('AN', 'Netherlands Antilles'),
    ('AO', 'Angola'),
    ('AQ', 'Antarctica'),
    ('AR', 'Argentina'),
    ('AS', 'American Samoa'),
    ('AT', 'Austria'),
    ('AU', 'Australia'),
    ('AW', 'Aruba'),
    ('AZ', 'Azerbaijan'),
    ('BA', 'Bosnia and Herzegovina'),
    ('BB', 'Barbados'),
    ('BD', 'Bangladesh'),
    ('BE', 'Belgium'),
    ('BF', 'Burkina Faso'),
    ('BG', 'Bulgaria'),
    ('BH', 'Bahrain'),
    ('BI', 'Burundi'),
    ('BJ', 'Benin'),
    ('BM', 'Bermuda'),
    ('BN', 'Brunei Darussalam'),
    ('BO', 'Bolivia'),
    ('BR', 'Brazil'),
    ('BS', 'Bahama'),
    ('BT', 'Bhutan'),
    ('BV', 'Bouvet Island'),
    ('BW', 'Botswana'),
    ('BY', 'Belarus'),
    ('BZ', 'Belize'),
    ('CA', 'Canada'),
    ('CC', 'Cocos (Keeling) Islands'),
    ('CF', 'Central African Republic'),
    ('CG', 'Congo'),
    ('CH', 'Switzerland'),
    ('CI', 'Ivory Coast'),
    ('CK', 'Cook Iislands'),
    ('CL', 'Chile'),
    ('CM', 'Cameroon'),
    ('CN', 'China'),
    ('CO', 'Colombia'),
    ('CR', 'Costa Rica'),
    ('CU', 'Cuba'),
    ('CV', 'Cape Verde'),
    ('CX', 'Christmas Island'),
    ('CY', 'Cyprus'),
    ('CZ', 'Czech Republic'),
    ('DE', 'Germany'),
    ('DJ', 'Djibouti'),
    ('DK', 'Denmark'),
    ('DM', 'Dominica'),
    ('DO', 'Dominican Republic'),
    ('DZ', 'Algeria'),
    ('EC', 'Ecuador'),
    ('EE', 'Estonia'),
    ('EG', 'Egypt'),
    ('EH', 'Western Sahara'),
    ('ER', 'Eritrea'),
    ('ES', 'Spain'),
    ('ET', 'Ethiopia'),
    ('FI', 'Finland'),
    ('FJ', 'Fiji'),
    ('FK', 'Falkland Islands (Malvinas)'),
    ('FM', 'Micronesia'),
    ('FO', 'Faroe Islands'),
    ('FR', 'France'),
    ('FX', 'France, Metropolitan'),
    ('GA', 'Gabon'),
    ('GB', 'United Kingdom (Great Britain)'),
    ('GD', 'Grenada'),
    ('GE', 'Georgia'),
    ('GF', 'French Guiana'),
    ('GH', 'Ghana'),
    ('GI', 'Gibraltar'),
    ('GL', 'Greenland'),
    ('GM', 'Gambia'),
    ('GN', 'Guinea'),
    ('GP', 'Guadeloupe'),
    ('GQ', 'Equatorial Guinea'),
    ('GR', 'Greece'),
    ('GS', 'South Georgia and the South Sandwich Islands'),
    ('GT', 'Guatemala'),
    ('GU', 'Guam'),
    ('GW', 'Guinea-Bissau'),
    ('GY', 'Guyana'),
    ('HK', 'Hong Kong'),
    ('HM', 'Heard & McDonald Islands'),
    ('HN', 'Honduras'),
    ('HR', 'Croatia'),
    ('HT', 'Haiti'),
    ('HU', 'Hungary'),
    ('ID', 'Indonesia'),
    ('IE', 'Ireland'),
    ('IL', 'Israel'),
    ('IN', 'India'),
    ('IO', 'British Indian Ocean Territory'),
    ('IQ', 'Iraq'),
    ('IR', 'Islamic Republic of Iran'),
    ('IS', 'Iceland'),
    ('IT', 'Italy'),
    ('JM', 'Jamaica'),
    ('JO', 'Jordan'),
    ('JP', 'Japan'),
    ('KE', 'Kenya'),
    ('KG', 'Kyrgyzstan'),
    ('KH', 'Cambodia'),
    ('KI', 'Kiribati'),
    ('KM', 'Comoros'),
    ('KN', 'St. Kitts and Nevis'),
    ('KP', 'Korea, Democratic People\'s Republic of'),
    ('KR', 'Korea, Republic of'),
    ('KW', 'Kuwait'),
    ('KY', 'Cayman Islands'),
    ('KZ', 'Kazakhstan'),
    ('LA', 'Lao People\'s Democratic Republic'),
    ('LK', 'Sri Lanka'),
    ('LV', 'Latvia'),
    ('LY', 'Libyan Arab Jamahiriya'),
    ('MA', 'Morocco'),
    ('MC', 'Monaco'),
    ('MD', 'Moldova, Republic of'),
    ('MG', 'Madagascar'),
    ('MH', 'Marshall Islands'),
    ('MN', 'Mongolia'),
    ('MM', 'Myanmar'),
    ('MO', 'Macau'),
    ('MP', 'Northern Mariana Islands'),
    ('MQ', 'Martinique'),
    ('MR', 'Mauritania'),
    ('MS', 'Monserrat'),
    ('MT', 'Malta'),
    ('MU', 'Mauritius'),
    ('MV', 'Maldives'),
    ('MW', 'Malawi'),
    ('MX', 'Mexico'),
    ('MY', 'Malaysia'),
    ('MZ', 'Mozambique'),
    ('NA', 'Namibia'),
    ('NC', 'New Caledonia'),
    ('NE', 'Niger'),
    ('NF', 'Norfolk Island'),
    ('NG', 'Nigeria'),
    ('NI', 'Nicaragua'),
    ('NL', 'Netherlands'),
    ('NO', 'Norway'),
    ('NP', 'Nepal'),
    ('NR', 'Nauru'),
    ('NU', 'Niue'),
    ('NZ', 'New Zealand'),
    ('OM', 'Oman'),
    ('PA', 'Panama'),
    ('PE', 'Peru'),
    ('PF', 'French Polynesia'),
    ('PG', 'Papua New Guinea'),
    ('PH', 'Philippines'),
    ('PK', 'Pakistan'),
    ('PL', 'Poland'),
    ('PM', 'St. Pierre & Miquelon'),
    ('PN', 'Pitcairn'),
    ('PR', 'Puerto Rico'),
    ('PT', 'Portugal'),
    ('PW', 'Palau'),
    ('PY', 'Paraguay'),
    ('QA', 'Qatar'),
    ('RE', 'Reunion'),
    ('RO', 'Romania'),
    ('RU', 'Russian Federation'),
    ('RW', 'Rwanda'),
    ('SA', 'Saudi Arabia'),
    ('SB', 'Solomon Islands'),
    ('SC', 'Seychelles'),
    ('SD', 'Sudan'),
    ('SE', 'Sweden'),
    ('SG', 'Singapore'),
    ('SH', 'St. Helena'),
    ('SI', 'Slovenia'),
    ('SJ', 'Svalbard & Jan Mayen Islands'),
    ('SK', 'Slovakia'),
    ('SL', 'Sierra Leone'),
    ('SM', 'San Marino'),
    ('SN', 'Senegal'),
    ('SO', 'Somalia'),
    ('SR', 'Suriname'),
    ('ST', 'Sao Tome & Principe'),
    ('SV', 'El Salvador'),
    ('SY', 'Syrian Arab Republic'),
    ('SZ', 'Swaziland'),
    ('TC', 'Turks & Caicos Islands'),
    ('TD', 'Chad'),
    ('TF', 'French Southern Territories'),
    ('TG', 'Togo'),
    ('TH', 'Thailand'),
    ('TJ', 'Tajikistan'),
    ('TK', 'Tokelau'),
    ('TM', 'Turkmenistan'),
    ('TN', 'Tunisia'),
    ('TO', 'Tonga'),
    ('TP', 'East Timor'),
    ('TR', 'Turkey'),
    ('TT', 'Trinidad & Tobago'),
    ('TV', 'Tuvalu'),
    ('TW', 'Taiwan, Province of China'),
    ('TZ', 'Tanzania, United Republic of'),
    ('UA', 'Ukraine'),
    ('UG', 'Uganda'),
    ('UM', 'United States Minor Outlying Islands'),
    ('US', 'United States of America'),
    ('UY', 'Uruguay'),
    ('UZ', 'Uzbekistan'),
    ('VA', 'Vatican City State (Holy See)'),
    ('VC', 'St. Vincent & the Grenadines'),
    ('VE', 'Venezuela'),
    ('VG', 'British Virgin Islands'),
    ('VI', 'United States Virgin Islands'),
    ('VN', 'Viet Nam'),
    ('VU', 'Vanuatu'),
    ('WF', 'Wallis & Futuna Islands'),
    ('WS', 'Samoa'),
    ('YE', 'Yemen'),
    ('YT', 'Mayotte'),
    ('YU', 'Yugoslavia'),
    ('ZA', 'South Africa'),
    ('ZM', 'Zambia'),
    ('ZR', 'Zaire'),
    ('ZW', 'Zimbabwe'),
    ('ZZ', 'Unknown or unspecified country'),
)

Select_Cuisines=(
    ('Thai','Thai'),
    ('Tea ', 'Tea'),
    ('Spanish ','Spanish'),
    ('Indian','Indian'),
    ('seafood','seafood'),
)
Select_Cost=(
    ('500 for 2 People','500 for 2 People'),
    ('1000 for 2 People ', '1000 for 2 People'),
    ('1500 for 2 People','1500 for 2 People'),
    ('2000 for 2 People','2000 for 2 People'),
    ('Above 2000 for 2 People','Above 2000 for 2 People'),
)

Select_Status=(
    ('Active','Active'),
    ('Deactive ', 'Deactive'),

)

    #def images_upload_tag(self):
      # return mark_safe('<a href="/media/{0}"><img src="/media/{0}"></a>'.format(self.images_upload))
   # images_upload_tag.short_description = ' restaurents Photos'
    #images_upload_tag.allow_tags = True

class Dining(models.Model):
    Name_of_Restaurant=models.CharField(max_length=200)
    Category=models.CharField(max_length=200, choices=Select_Category)
    Rating=models.CharField(max_length=200, choices=Select_Rating)
    City=models.CharField(max_length=200, choices=Select_City)
    Area=models.CharField(max_length=200, choices=Select_Area)
    State=models.CharField(max_length=200, choices=Select_State)
    #State = models.USStateField(choices=STATE_CHOICES)
    #State = models.CharField(max_length=2, choices=STATE_CHOICES, null=True, blank=True)  
    Country=models.TextField(max_length=1000, choices=Select_Country)
    #Country = CountryField(multiple=True)
    #Country = models.ChoiceField(sorted(COUNTRIES.items()))
    Pin_Code=models.CharField(max_length=200)
    Helpline_Number=models.CharField(max_length=200)
    Cuisines=models.CharField(max_length=200, choices=Select_Cuisines)
    Average_Cost=models.CharField(max_length=200, choices=Select_Cost)
    Address=models.TextField(max_length=200)
    Brief_Overview =models.TextField(max_length=200,default='')
    Active_Status=models.CharField(max_length=200, choices=Select_Status,default='')
    Added_on=models.DateField(default='')
    #images_upload = models.ImageField(upload_to='dining/files',default="")
    file_upload = models.FileField(upload_to='dining/files',default="")
class Restaurants_images(models.Model):
    dining=models.ForeignKey(Dining, on_delete=models.CASCADE, related_name='dining')
    images_upload = models.ImageField(upload_to='dining/images',default="")



class VendorsRestaurant_search(models.Model):
    Rating=models.CharField(max_length=200, choices=Select_Rating)
    City=models.CharField(max_length=200, choices=Select_City)
    Area=models.CharField(max_length=200, choices=Select_Area)
    Cuisines=models.CharField(max_length=200, choices=Select_Cuisines)


     