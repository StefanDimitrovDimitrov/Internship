from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


from Internship.internship_profiles.validators import company_phone_validator_len, company_phone_validator_digits
UserModel = get_user_model()
#
# def company_name_validator_unique(value):
#     all_companies = CompanyProfile.objects.all()
#     for company in all_companies:
#         if company.company_name != '' and company.company_name == value:
#
#             raise ValidationError("A company with this name already exists")


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

    email = models.EmailField(
        unique=True,
    )

    profile_image = models.ImageField(
        upload_to='intern_profile',
        default='InitialProfilePics/pic.png',
    )

    CV = models.FileField(
        upload_to='intern_cv',
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
        # validators=[company_name_validator_unique],
        blank=True,
    )

    email = models.EmailField(
        unique=True,
    )

    company_logo = models.ImageField(
        upload_to='company_logo',
        default='InitialProfilePics/Logo.jpg',
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
                                     validators=[company_phone_validator_len,company_phone_validator_digits],
                                     help_text='The number should contain 10 digits')

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




