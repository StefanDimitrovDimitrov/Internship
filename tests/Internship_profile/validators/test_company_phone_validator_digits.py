from django.core.exceptions import ValidationError
from django.test import TestCase

from Internship.internship_profiles.validators import company_phone_validator_digits


class ValidatePhoneNumDigitsTests(TestCase):
    def test_whenPhoneNumContainsLetters_expectedToRaise(self):
        value = '0123iu'
        with self.assertRaises(ValidationError) as context:
            company_phone_validator_digits(value)

        self.assertIsNotNone(context.exception)

    def test_whenPhoneNumContainsOnlyNumbers_expectToNothing(self):
        value = '000000000000000000000'
        company_phone_validator_digits(value)