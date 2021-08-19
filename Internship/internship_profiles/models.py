from django.contrib.auth import get_user_model
from django.db import models

from Internship.internship_profiles.validators import company_phone_validator_len, company_phone_validator_digits

UserModel = get_user_model()
from cloudinary import models as cloudinary_model

class CandidateProfile(models.Model):
    first_name = models.CharField(
        max_length=20,
        blank=True,
    )

    last_name = models.CharField(
        max_length=20,
        blank=True,
    )

    email = models.EmailField(
        unique=True,
    )

    profile_image = cloudinary_model.CloudinaryField(
        resource_type='image',
        blank=True,
    )

    CV = cloudinary_model.CloudinaryField(
        resource_type='image',
        blank=True,
    )

    is_complete = models.BooleanField(
        default=False
    )

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True
    )

    def __str__(self):
        return self.email


class CompanyProfile(models.Model):
    company_name = models.CharField(
        max_length=35,
        blank=True,
    )

    email = models.EmailField(
        unique=True,
    )

    company_logo = cloudinary_model.CloudinaryField(
        resource_type='image',
        blank=True,
    )

    description = models.TextField(
        max_length=500,
        blank=True,
    )

    company_website = models.URLField(
        blank=True
    )

    company_address = models.CharField(
        max_length=50,
        blank=True
    )

    company_phone = models.CharField(max_length=20,
                                     blank=True,
                                     validators=[company_phone_validator_len, company_phone_validator_digits])

    is_complete = models.BooleanField(
        default=False
    )

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True
    )

    def __str__(self):
        return self.email
