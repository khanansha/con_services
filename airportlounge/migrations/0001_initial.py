# Generated by Django 2.2.10 on 2020-03-23 13:01

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AirportLounge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name_of_Lounge', models.CharField(max_length=50)),
                ('City', models.CharField(choices=[('mumbai', 'Mumbai'), ('delhi', 'Delhi'), ('Bangalore', 'Bangalore'), ('Hyderabad', 'Hyderabad'), ('Ahmedabad', 'Ahmedabad')], max_length=200)),
                ('Airport', models.CharField(max_length=100)),
                ('Country', models.CharField(choices=[('AD', 'Andorra'), ('AE', 'United Arab Emirates'), ('AF', 'Afghanistan'), ('AG', 'Antigua & Barbuda'), ('AI', 'Anguilla'), ('AL', 'Albania'), ('AM', 'Armenia'), ('AN', 'Netherlands Antilles'), ('AO', 'Angola'), ('AQ', 'Antarctica'), ('AR', 'Argentina'), ('AS', 'American Samoa'), ('AT', 'Austria'), ('AU', 'Australia'), ('AW', 'Aruba'), ('AZ', 'Azerbaijan'), ('BA', 'Bosnia and Herzegovina'), ('BB', 'Barbados'), ('BD', 'Bangladesh'), ('BE', 'Belgium'), ('BF', 'Burkina Faso'), ('BG', 'Bulgaria'), ('BH', 'Bahrain'), ('BI', 'Burundi'), ('BJ', 'Benin'), ('BM', 'Bermuda'), ('BN', 'Brunei Darussalam'), ('BO', 'Bolivia'), ('BR', 'Brazil'), ('BS', 'Bahama'), ('BT', 'Bhutan'), ('BV', 'Bouvet Island'), ('BW', 'Botswana'), ('BY', 'Belarus'), ('BZ', 'Belize'), ('CA', 'Canada'), ('CC', 'Cocos (Keeling) Islands'), ('CF', 'Central African Republic'), ('CG', 'Congo'), ('CH', 'Switzerland'), ('CI', 'Ivory Coast'), ('CK', 'Cook Iislands'), ('CL', 'Chile'), ('CM', 'Cameroon'), ('CN', 'China'), ('CO', 'Colombia'), ('CR', 'Costa Rica'), ('CU', 'Cuba'), ('CV', 'Cape Verde'), ('CX', 'Christmas Island'), ('CY', 'Cyprus'), ('CZ', 'Czech Republic'), ('DE', 'Germany'), ('DJ', 'Djibouti'), ('DK', 'Denmark'), ('DM', 'Dominica'), ('DO', 'Dominican Republic'), ('DZ', 'Algeria'), ('EC', 'Ecuador'), ('EE', 'Estonia'), ('EG', 'Egypt'), ('EH', 'Western Sahara'), ('ER', 'Eritrea'), ('ES', 'Spain'), ('ET', 'Ethiopia'), ('FI', 'Finland'), ('FJ', 'Fiji'), ('FK', 'Falkland Islands (Malvinas)'), ('FM', 'Micronesia'), ('FO', 'Faroe Islands'), ('FR', 'France'), ('FX', 'France, Metropolitan'), ('GA', 'Gabon'), ('GB', 'United Kingdom (Great Britain)'), ('GD', 'Grenada'), ('GE', 'Georgia'), ('GF', 'French Guiana'), ('GH', 'Ghana'), ('GI', 'Gibraltar'), ('GL', 'Greenland'), ('GM', 'Gambia'), ('GN', 'Guinea'), ('GP', 'Guadeloupe'), ('GQ', 'Equatorial Guinea'), ('GR', 'Greece'), ('GS', 'South Georgia and the South Sandwich Islands'), ('GT', 'Guatemala'), ('GU', 'Guam'), ('GW', 'Guinea-Bissau'), ('GY', 'Guyana'), ('HK', 'Hong Kong'), ('HM', 'Heard & McDonald Islands'), ('HN', 'Honduras'), ('HR', 'Croatia'), ('HT', 'Haiti'), ('HU', 'Hungary'), ('ID', 'Indonesia'), ('IE', 'Ireland'), ('IL', 'Israel'), ('IN', 'India'), ('IO', 'British Indian Ocean Territory'), ('IQ', 'Iraq'), ('IR', 'Islamic Republic of Iran'), ('IS', 'Iceland'), ('IT', 'Italy'), ('JM', 'Jamaica'), ('JO', 'Jordan'), ('JP', 'Japan'), ('KE', 'Kenya'), ('KG', 'Kyrgyzstan'), ('KH', 'Cambodia'), ('KI', 'Kiribati'), ('KM', 'Comoros'), ('KN', 'St. Kitts and Nevis'), ('KP', "Korea, Democratic People's Republic of"), ('KR', 'Korea, Republic of'), ('KW', 'Kuwait'), ('KY', 'Cayman Islands'), ('KZ', 'Kazakhstan'), ('LA', "Lao People's Democratic Republic"), ('LK', 'Sri Lanka'), ('LV', 'Latvia'), ('LY', 'Libyan Arab Jamahiriya'), ('MA', 'Morocco'), ('MC', 'Monaco'), ('MD', 'Moldova, Republic of'), ('MG', 'Madagascar'), ('MH', 'Marshall Islands'), ('MN', 'Mongolia'), ('MM', 'Myanmar'), ('MO', 'Macau'), ('MP', 'Northern Mariana Islands'), ('MQ', 'Martinique'), ('MR', 'Mauritania'), ('MS', 'Monserrat'), ('MT', 'Malta'), ('MU', 'Mauritius'), ('MV', 'Maldives'), ('MW', 'Malawi'), ('MX', 'Mexico'), ('MY', 'Malaysia'), ('MZ', 'Mozambique'), ('NA', 'Namibia'), ('NC', 'New Caledonia'), ('NE', 'Niger'), ('NF', 'Norfolk Island'), ('NG', 'Nigeria'), ('NI', 'Nicaragua'), ('NL', 'Netherlands'), ('NO', 'Norway'), ('NP', 'Nepal'), ('NR', 'Nauru'), ('NU', 'Niue'), ('NZ', 'New Zealand'), ('OM', 'Oman'), ('PA', 'Panama'), ('PE', 'Peru'), ('PF', 'French Polynesia'), ('PG', 'Papua New Guinea'), ('PH', 'Philippines'), ('PK', 'Pakistan'), ('PL', 'Poland'), ('PM', 'St. Pierre & Miquelon'), ('PN', 'Pitcairn'), ('PR', 'Puerto Rico'), ('PT', 'Portugal'), ('PW', 'Palau'), ('PY', 'Paraguay'), ('QA', 'Qatar'), ('RE', 'Reunion'), ('RO', 'Romania'), ('RU', 'Russian Federation'), ('RW', 'Rwanda'), ('SA', 'Saudi Arabia'), ('SB', 'Solomon Islands'), ('SC', 'Seychelles'), ('SD', 'Sudan'), ('SE', 'Sweden'), ('SG', 'Singapore'), ('SH', 'St. Helena'), ('SI', 'Slovenia'), ('SJ', 'Svalbard & Jan Mayen Islands'), ('SK', 'Slovakia'), ('SL', 'Sierra Leone'), ('SM', 'San Marino'), ('SN', 'Senegal'), ('SO', 'Somalia'), ('SR', 'Suriname'), ('ST', 'Sao Tome & Principe'), ('SV', 'El Salvador'), ('SY', 'Syrian Arab Republic'), ('SZ', 'Swaziland'), ('TC', 'Turks & Caicos Islands'), ('TD', 'Chad'), ('TF', 'French Southern Territories'), ('TG', 'Togo'), ('TH', 'Thailand'), ('TJ', 'Tajikistan'), ('TK', 'Tokelau'), ('TM', 'Turkmenistan'), ('TN', 'Tunisia'), ('TO', 'Tonga'), ('TP', 'East Timor'), ('TR', 'Turkey'), ('TT', 'Trinidad & Tobago'), ('TV', 'Tuvalu'), ('TW', 'Taiwan, Province of China'), ('TZ', 'Tanzania, United Republic of'), ('UA', 'Ukraine'), ('UG', 'Uganda'), ('UM', 'United States Minor Outlying Islands'), ('US', 'United States of America'), ('UY', 'Uruguay'), ('UZ', 'Uzbekistan'), ('VA', 'Vatican City State (Holy See)'), ('VC', 'St. Vincent & the Grenadines'), ('VE', 'Venezuela'), ('VG', 'British Virgin Islands'), ('VI', 'United States Virgin Islands'), ('VN', 'Viet Nam'), ('VU', 'Vanuatu'), ('WF', 'Wallis & Futuna Islands'), ('WS', 'Samoa'), ('YE', 'Yemen'), ('YT', 'Mayotte'), ('YU', 'Yugoslavia'), ('ZA', 'South Africa'), ('ZM', 'Zambia'), ('ZR', 'Zaire'), ('ZW', 'Zimbabwe'), ('ZZ', 'Unknown or unspecified country')], max_length=10)),
                ('Facilities', multiselectfield.db.fields.MultiSelectField(choices=[('WIFI', 'WIFI'), ('Food', 'Food'), ('Alcohol', 'Alcohol'), ('Shower', 'Shower'), ('Sleeping Pod', 'Sleeping Pod')], max_length=10)),
                ('Terminal', models.CharField(max_length=100)),
                ('Service_Range', models.CharField(choices=[('India', 'India'), ('International', 'International')], max_length=10)),
                ('Package_Details', models.TextField(max_length=100)),
                ('Brief_Over', models.TextField(max_length=500)),
                ('Status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=0)),
                ('AddedOn', models.DateField()),
            ],
        ),
    ]
