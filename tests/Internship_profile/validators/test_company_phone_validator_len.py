from django.core.exceptions import ValidationError
from django.test import TestCase

from Internship.internship_profiles.validators import company_phone_validator_len


class ValidatePhoneNumLen(TestCase):
    def test_PhoneNumIsTenDigits_expectToDoNothing(self):
        value = '0123456789'
        company_phone_validator_len(value)


    def test_PhoneNumIsBiggerThenTenDigits_expectToRaise(self):
        value = '0123'
        with self.assertRaises(ValidationError) as context:
            company_phone_validator_len(value)

        self.assertIsNotNone(context.exception)

    def test_PhoneNumIsLessThenTenDigits_expectToRaise(self):
        value = '1234567899999999'
        with self.assertRaises(ValidationError) as context:
            company_phone_validator_len(value)

        self.assertIsNotNone(context.exception)
