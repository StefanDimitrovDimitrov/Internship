# Generated by Django 3.2.5 on 2021-07-20 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internship_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internshipuser',
            name='profile',
            field=models.CharField(blank=True, choices=[('Company', 'Company'), ('Candidate', 'Candidate')], max_length=10),
        ),
    ]
