# Generated by Django 3.2.5 on 2021-07-20 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internship_auth', '0002_alter_internshipuser_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internshipuser',
            name='profile',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
