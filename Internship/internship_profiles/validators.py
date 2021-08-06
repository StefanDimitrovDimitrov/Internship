from django.core.exceptions import ValidationError


def company_phone_validator_len(value):
    if len(value) != 10:
        raise ValidationError('Error with the Company Phone number')


def company_phone_validator_digits(value):
    try:
        [int(d) for d in value]
    except ValueError:
        raise ValidationError('Error with the Company Phone number')
