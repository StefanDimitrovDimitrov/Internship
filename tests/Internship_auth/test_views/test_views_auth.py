import email.charset
from datetime import datetime

from django.contrib.auth import get_user_model, logout
from django.db.utils import IntegrityError
from django.http import request
from django.test import TestCase, Client
from django.urls import reverse

from Internship.internship_app.models import Internship_ad
from Internship.internship_auth.models import InternshipUser
from Internship.internship_profiles.models import CompanyProfile, CandidateProfile

UserModel = get_user_model()


class TestAuth(TestCase):
    def setUp(self):
        self.client = Client()

        self.register_candidate_url = reverse('register candidate')
        self.register_company_url = reverse('register company')



    def test_register_candidate_POST_expect_user_candidate_and_candidate_profile_to_be_created(self):
        response = self.client.post(self.register_candidate_url,
                                    {'email': 'C1@gmail.com', 'password1': 'Donatelo123!', 'password2': 'Donatelo123!'})

        get_user_candidate = UserModel.objects.first()
        get_all_candidates = CandidateProfile.objects.all()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(get_all_candidates), 1)
        self.assertEqual(get_user_candidate.id, get_all_candidates[0].user_id)

    def test_register_candidate_twice_same_email_POST_raise_validation_Error(self):
        self.user_candidate = UserModel.objects.create_user(email='C1@gmail.com', password='Donatelo123!',
                                                            profile='Candidate')
        self.assertTrue(InternshipUser.objects.all())
        with self.assertRaises(IntegrityError):
            self.user_candidate2 = UserModel.objects.create_user(email='C1@gmail.com', password='Donatelo123!',
                                                                 profile='Candidate')


    def test_change_candidate_credentials_password_POST_successfully(self):
        response = self.client.post(self.register_candidate_url,
                                    {'email': 'C1@gmail.com', 'password1': 'Donatelo123!', 'password2': 'Donatelo123!'})
        get_candidate = CandidateProfile.objects.first()
        self.assertEqual(get_candidate.email, 'C1@gmail.com')
        get_user_candidate = UserModel.objects.get(id=get_candidate.user_id)
        pass1 = get_user_candidate.password
        test_change_candidate_credential_url = reverse('change candidate credentials',
                                                            args=[get_candidate.user_id])

        response = self.client.post(test_change_candidate_credential_url,
                                    {'old_password': 'Donatelo123!', 'new_password1': 'Donatelo1234!', 'new_password2': 'Donatelo1234!'})

        get_user_candidate = UserModel.objects.get(id = get_candidate.user_id)
        pass2 = get_user_candidate.password

        self.assertNotEqual(pass1, pass2)



    def test_register_company_POST(self):
        response = self.client.post(self.register_company_url,
                                    {'email': 'Company1@gmail.com', 'password1': 'Donatelo123!', 'password2': 'Donatelo123!'})

        get_user_company = UserModel.objects.first()
        get_all_companies = CompanyProfile.objects.all()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(get_all_companies ), 1)
        self.assertEqual(get_user_company.id, get_all_companies[0].user_id)

    def test_register_company_same_email_POST_not_possible_expect_error(self):
        self.user_company = UserModel.objects.create_user(email='Company1@gmail.com', password='Donatelo123!',
                                                          profile='Company')

        with self.assertRaises(IntegrityError):
            self.user_company = UserModel.objects.create_user(email='Company1@gmail.com', password='Donatelo123!',
                                                              profile='Company')


    def test_change_company_credentials_password_successfully_POST(self):
        response = self.client.post(self.register_company_url,
                                    {'email': 'Company1@gmail.com', 'password1': 'Donatelo123!', 'password2': 'Donatelo123!'})
        get_company = CompanyProfile.objects.first()
        self.assertEqual(get_company.email, 'Company1@gmail.com')
        get_user_company = UserModel.objects.get(id=get_company.user_id)
        pass1 = get_user_company.password
        test_change_company_credential_url = reverse('change company credentials',
                                                       args=[get_company.user_id])

        response = self.client.post(test_change_company_credential_url,
                                    {'old_password': 'Donatelo123!', 'new_password1': 'Donatelo1234!', 'new_password2': 'Donatelo1234!'})

        get_user_company = UserModel.objects.get(id=get_company.user_id)
        pass2 = get_user_company.password

        self.assertNotEqual(pass1, pass2)