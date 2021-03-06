# Generated by Django 3.2.5 on 2021-08-17 12:33

import Internship.internship_profiles.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('internship_auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CandidateProfile',
            fields=[
                ('first_name', models.CharField(blank=True, max_length=20)),
                ('last_name', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('profile_image', models.ImageField(default='InitialProfilePics/pic.png', upload_to='intern_profile')),
                ('CV', models.FileField(blank=True, upload_to='intern_cv')),
                ('is_complete', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='internship_auth.internshipuser')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('company_name', models.CharField(blank=True, max_length=35)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('company_logo', models.ImageField(default='InitialProfilePics/Logo.jpg', upload_to='company_logo')),
                ('description', models.TextField(blank=True, max_length=500)),
                ('company_website', models.URLField(blank=True)),
                ('company_address', models.CharField(blank=True, max_length=50)),
                ('company_phone', models.CharField(blank=True, max_length=20, validators=[Internship.internship_profiles.validators.company_phone_validator_len, Internship.internship_profiles.validators.company_phone_validator_digits])),
                ('is_complete', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='internship_auth.internshipuser')),
            ],
        ),
    ]
