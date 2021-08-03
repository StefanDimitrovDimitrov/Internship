from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator


def company_phone_validator(value):
    if value.length < 10:
        raise ValidationError('The phone number should contains 10 numbers')


def company_name_validator(value):
    MinLengthValidator(6)(value)
    if value[0] != value[0].upper():
        raise ValidationError('The name mus start with an uppercase letter')
