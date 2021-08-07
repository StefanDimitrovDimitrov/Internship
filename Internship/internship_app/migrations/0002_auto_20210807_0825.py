# Generated by Django 3.2.5 on 2021-08-07 05:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internship_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appliedtracking',
            old_name='applied_candidate',
            new_name='applied_candidates',
        ),
        migrations.RenameField(
            model_name='appliedtracking',
            old_name='internship_ad',
            new_name='internship_ads',
        ),
        migrations.AlterField(
            model_name='internship_ad',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 7, 8, 25, 32, 52538), editable=False),
        ),
    ]
