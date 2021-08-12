import email.charset
from datetime import datetime

from django.contrib.auth import get_user_model, logout
from django.db.utils import IntegrityError
from django.http import request
from django.test import TestCase, Client
from django.urls import reverse

from Internship.internship_app.models import Internship_ad
from Internship.internship_profiles.models import CompanyProfile, CandidateProfile

UserModel = get_user_model()


class TestAuth(TestCase):
    def setUp(self):
        self.client = Client()


    def test_register_candidate_POST(self):
        self.user_candidate = UserModel.objects.create_user(email='C1@gmail.com', password='Donatelo123!',
                                                            profile='Candidate')

        get_all_candidates = CandidateProfile.objects.all()

        self.assertEqual(len(get_all_candidates), 1)
        self.assertEqual(self.user_candidate.id, get_all_candidates[0].user_id)

    def test_register_candidate_same_email_POST(self):
        self.user_candidate = UserModel.objects.create_user(email='C1@gmail.com', password='Donatelo123!',
                                                            profile='Candidate')

        with self.assertRaises(IntegrityError):
            self.user_candidate2 = UserModel.objects.create_user(email='C1@gmail.com', password='Donatelo123!',
                                                                 profile='Candidate')

    def test_change_candidate_credentials_email_POST(self):
        self.user_candidate = UserModel.objects.create_user(email='C1@gmail.com', password='Donatelo123!',
                                                            profile='Candidate')


        self.user_candidate.email = 'C2@email.com'
        self.user_candidate.save()
        self.assertEqual(self.user_candidate.email, 'C2@email.com')
        get_current_candidate = CandidateProfile.objects.get(user_id=self.user_candidate.id)
        get_current_candidate.email = self.user_candidate.email


        self.assertEqual(get_current_candidate.email, 'C2@email.com')

    def test_change_candidate_credentials_password_POST(self):
        self.user_candidate = UserModel.objects.create_user(email='C1@gmail.com', password='Donatelo123!',
                                                            profile='Candidate')
        self.client.force_login(self.user_candidate)
        self.user_candidate.password = 'Donatelo1234!'
        self.client.logout()

        self.assertEqual(self.user_candidate.password, 'Donatelo1234!')
        self.client.force_login(self.user_candidate)

    def test_register_company_POST(self):
        self.user_company = UserModel.objects.create_user(email='Company1@gmail.com', password='Donatelo123!',
                                                            profile='Company')

        get_all_companies = CompanyProfile.objects.all()

        self.assertEqual(len(get_all_companies), 1)
        self.assertEqual(self.user_company.id, get_all_companies[0].user_id)

    def test_register_company_same_email_POST(self):
        self.user_company = UserModel.objects.create_user(email='Company1@gmail.com', password='Donatelo123!',
                                                          profile='Company')

        with self.assertRaises(IntegrityError):
            self.user_company = UserModel.objects.create_user(email='Company1@gmail.com', password='Donatelo123!',
                                                              profile='Company')

    def test_change_company_credentials_password_POST(self):
        self.user_company = UserModel.objects.create_user(email='Company1@gmail.com', password='Donatelo123!',
                                                          profile='Company')


        self.client.force_login(self.user_company)
        self.user_company.password = 'Donatelo1234!'
        self.client.logout()

        self.assertEqual(self.user_company.password, 'Donatelo1234!')
        self.client.force_login(self.user_company)

    def test_change_company_credentials_email_POST(self):
        self.user_company = UserModel.objects.create_user(email='Company1@gmail.com', password='Donatelo123!',
                                                          profile='Company')


        self.user_company.email = 'Company2@email.com'
        self.user_company.save()
        self.assertEqual(self.user_company.email, 'Company2@email.com')
        get_current_company = CompanyProfile.objects.get(user_id=self.user_company.id)
        get_current_company.email = self.user_company.email

        self.assertEqual(get_current_company.email, 'Company2@email.com')


