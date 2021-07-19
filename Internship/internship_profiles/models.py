from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


# Create your models here.
class CandidateProfile(models.Model):
    first_name = models.CharField(
        max_length=20,
        blank=True,

    )
    last_name = models.CharField(
        max_length=20,
        blank=True,

    )
    profile_image = models.ImageField(
        upload_to='intern_profile',
        blank=True,

    )
    CV = models.FileField(
        upload_to='intern_cv',
        blank=True,

    )
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
    )


class CompanyProfile(models.Model):
    company_name = models.CharField(
        max_length=35,
        blank=True,

    )

    company_logo = models.ImageField(
        upload_to='company_logo',
        blank=True,

    )

    description = models.ImageField(
        max_length=500,
        blank=True,

    )

    company_image = models.ImageField(
        upload_to='company_pics',
        blank=True,
    )

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    # list of ads
