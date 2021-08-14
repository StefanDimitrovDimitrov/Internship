from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase, Client

from django.test import SimpleTestCase

from Internship.internship_auth.forms import RegisterForm, ChangePassword, LoginForm


UserModel = get_user_model()


class TestForms1(TestCase):
    def setUp(self):
        self.client = Client()

        self.user= UserModel.objects.create_user(email='Google@gmail.com', password='Donatelo12!', profile='Company')

    def test_register_form_valid_data(self):

        form = RegisterForm({
            'email':"mail@mail.bg",
            'password1': 'Donatelo123!',
            'password2': 'Donatelo123!',
        })

        self.assertTrue(form.is_valid())

    def test_register_form_no_data(self):

        form = RegisterForm({

        })

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)

    def test_register_form_password_no_match(self):

        form = RegisterForm({
            'email':"mail@mail.bg",
            'password1': 'Donatelo1234!',
            'password2': 'Donatelo123!',
        })

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)


    def test_login_form_form_is_valid_data(self):
        form = LoginForm({
            'email': 'Google@gmail.com',
            'password': 'Donatelo12!',
        })

        self.assertTrue(form.is_valid())


    def test_login_form_form_is_not_valid(self):
        form = LoginForm({

        })

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)

    def test_login_form_form_is_not_valid_password(self):
        form = LoginForm({
            'email': 'Google@gmail.com',
            'password': 'Donatelo124!',
        })

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),1)