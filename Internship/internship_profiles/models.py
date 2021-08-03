from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from phone_field import PhoneField

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


def company_phone_validator_len(value):
    if len(value) < 10:
        raise ValidationError('Error with the Company Phone number')


def company_phone_validator_digits(value):
    try:
        [int(d) for d in value]
    except ValueError:
        raise ValidationError('Error with the Company Phone number')


class CompanyProfile(models.Model):
    company_name = models.CharField(
        max_length=35,
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
        max_length=20,
        blank=True
    )

    company_phone = models.CharField(max_length=20,
                                     blank=True, validators=[company_phone_validator_len,company_phone_validator_digits])
    # help_text='Contact phone number')

    is_complete = models.BooleanField(
        default=False
    )

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True
    )

#


# def company_name_validator(value):
#     MinLengthValidator(6)(value)
#     if value[0] != value[0].upper():
#         raise ValidationError('The name mus start with an uppercase letter')
