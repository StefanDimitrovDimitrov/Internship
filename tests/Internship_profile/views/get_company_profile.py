from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from Internship.internship_app.models import Internship_ad
from Internship.internship_profiles.models import CompanyProfile

UserModel = get_user_model()


class CompanyProfileTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(email='Google@gmail.com', password='Donatelo123!', profile='Company')

    def test_getProfile_whenLoggedInUser_shouldGetProfile(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('company profile', args=[1]))

        self.assertListEqual([], list(response.context['company_ads']))

    def test_getProfile_whenLoggedInUserwithAds_shouldGetProfileWithAds(self):
        current_company = CompanyProfile.objects.get(user_id=self.user.id)
        adv = Internship_ad.objects.create(
            created_at=datetime.now(),
            modified_at=datetime.now(),
            title='Test Ad',
            city='Sofia',
            field='Information Technology',
            employment_type='full-time',
            duration='1 month',
            image='path/to/image.png',
            description='asdhadhakljdh',
            is_active=True,
            company_owner=current_company
        )

        self.client.force_login(self.user)
        response = self.client.get(reverse('company profile', args=[1]))


        self.assertEqual(adv.company_owner, current_company)
