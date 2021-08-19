# Generated by Django 3.2.6 on 2021-08-19 08:04

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('internship_profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidateprofile',
            name='profile_image',
            field=cloudinary.models.CloudinaryField(default='InitialProfilePics/pic.png', max_length=255),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='company_logo',
            field=cloudinary.models.CloudinaryField(default='InitialProfilePics/Logo.jpg', max_length=255),
        ),
    ]
