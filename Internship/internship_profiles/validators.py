from django.core.exceptions import ValidationError




def company_phone_validator_len(value):
    if len(value) != 10:
        raise ValidationError('The phone number should contain 10 digits')


def company_phone_validator_digits(value):
    try:
        [int(d) for d in value]
    except ValueError:
        raise ValidationError('The company number has to contain only digits')




