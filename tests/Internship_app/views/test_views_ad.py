from datetime import datetime

from django.contrib.auth.models import User
from django.http import request
from django.urls import reverse, resolve
from django.test import TestCase, Client

from Internship.internship_app.models import Internship_ad, AppliedTracking
from Internship.internship_app.views import edit_ad
from Internship.internship_auth.models import InternshipUser
from Internship.internship_profiles.models import CompanyProfile, UserModel, CandidateProfile


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user_company = UserModel.objects.create_user(email='Google@gmail.com', password='Donatelo123!', profile='Company')
        self.user_candidate = UserModel.objects.create_user(email='Google1@gmail.com', password='Donatelo123!', profile='Candidate')
        self.current_company = CompanyProfile.objects.get(user_id=self.user_company.id)
        self.current_candidate = CandidateProfile.objects.get(user_id=self.user_candidate.id)

        self.adv1 = Internship_ad.objects.create(
            created_at='2021-09-04 06:00:00.000000',
            modified_at='2021-09-04 06:00:00.000000',
            title='Test Ad',
            city='Sofia',
            field='Information Technology',
            employment_type='Full-Time',
            duration='1 month',
            description='Some test description',
            is_active=True,
            company_owner=self.current_company
        )

        self.list_url = reverse('home')
        self.details_url = reverse('details ad', args=[self.adv1.id])
        self.create_url = reverse('create ad')
        self.company_catalog_url = reverse('catalog companies')
        self.edit_url = reverse('edit ad', args=[self.adv1.id])
        self.delete_url = reverse('delete ad', args=[self.adv1.id])
        self.deactivate_url = reverse('deactivate ad', args=[self.adv1.id])
        self.activate_url = reverse('activate ad', args=[self.adv1.id])
        self.apply_url = reverse('apply', args=[self.adv1.id])



    def test_home_GET(self):
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shared/../../templates/main/base.html')

    def test_company_catalog_GET(self):
        response = self.client.get(self.company_catalog_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'internship/catalog_companies.html')

    def test_ad_details_GET(self):
        self.client.force_login(self.user_company)
        response = self.client.get(self.details_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'internship/details_ad.html')

    def test_ad_create_GET(self):
        self.client.force_login(self.user_company)
        response = self.client.get(self.create_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'internship/create_ad.html')

    def test_ad_create_POST_successfully(self):
        self.client.force_login(self.user_company)
        response = self.client.post(self.create_url,{
            'created_at': '2021-09-04 06:00:00.000000',
            'modified_at': '2021-09-04 06:00:00.000000',
            'title': 'FirstAd',
            'city': 'Plovdiv',
            'field': 'Information Technology',
            'employment_type': 'Full-Time',
            'duration': '1 month',
            'description': 'Some test description',
            'is_active': True,
            'company_owner': self.current_company
        })

        self.assertEqual(response.status_code, 302)
        adv = Internship_ad.objects.filter(title__icontains='FirstAd')[0]
        self.assertEquals(adv.title, 'FirstAd')
        self.assertEquals(adv.city, 'Plovdiv')
        self.assertEquals(adv.duration, '1 month')
        self.assertEquals(adv.company_owner, self.current_company)

    def test_ad_edit_POST(self):
        self.client.force_login(self.user_company)
        response = self.client.post(self.edit_url, {
            'created_at': '2021-09-04 06:00:00.000000',
            'modified_at': '2021-09-04 06:00:00.000000',
            'title': 'TitleChanged',
            'city': 'Sofia',
            'field': 'Information Technology',
            'employment_type': 'Full-Time',
            'duration': '1 month',
            'description': 'Some test description',
            'is_active': True,
            'company_owner': self.current_company
        })
        change_ad = Internship_ad.objects.first()
        self.assertEqual(response.status_code, 302)
        self.assertEquals(change_ad.title, 'TitleChanged')


    def test_ad_deactivate_POST(self):
        self.client.force_login(self.user_company)
        self.adv1.is_active = True
        response = self.client.post(self.deactivate_url,{self.adv1.is_active:False})

        current_ad = Internship_ad.objects.get(id=self.adv1.id)
        self.assertEqual(response.status_code, 302)
        self.assertEquals(current_ad.is_active, False)

    def test_ad_activate_POST(self):
        self.client.force_login(self.user_company)

        self.adv1.is_active = False

        response = self.client.get(self.activate_url,{self.adv1.is_active:True})

        self.adv1.is_active = True
        current_ad = Internship_ad.objects.get(id=self.adv1.id)
        self.assertEqual(response.status_code, 302)
        self.assertEquals(current_ad.is_active, True)

    def test_ad_apply_POST(self):

        self.client.force_login(self.user_candidate)
        response = self.client.post(self.apply_url,{self.current_candidate.CV: 'intern_cv/new_cv.docx'})

        new_applied_candidate = AppliedTracking()

        self.assertEqual(response.status_code, 200)
        self.assertEquals(new_applied_candidate.CV, self.current_candidate.CV)

    def test_ad_delete_POST(self):
        self.client.force_login(self.user_company)
        response = self.client.post(self.delete_url)

        self.adv1.delete()

        self.assertEqual(response.status_code, 302)
        self.assertEquals(len(Internship_ad.objects.all()), 0)
