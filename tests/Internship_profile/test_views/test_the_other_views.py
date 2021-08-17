from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from Internship.internship_app.models import Internship_ad
from Internship.internship_profiles.models import CompanyProfile, CandidateProfile

UserModel = get_user_model()


class TestProfiles(TestCase):
    def setUp(self):
        self.client = Client()
        self.user_company = UserModel.objects.create_user(email='Google@gmail.com', password='Donatelo123!',
                                                          profile='Company')
        self.user_candidate = UserModel.objects.create_user(email='C1@gmail.com', password='Donatelo123!',
                                                            profile='Candidate')
        self.current_company = CompanyProfile.objects.get(user_id=self.user_company.id)
        self.current_candidate = CandidateProfile.objects.get(user_id=self.user_candidate.id)

        self.adv2 = Internship_ad.objects.create(
            created_at=datetime.now(),
            modified_at=datetime.now(),
            title='Test Ad2',
            city='Sofia',
            field='Information Technology',
            employment_type='Full-Time',
            duration='1 month',
            description='asdhadhakljdh',
            is_active=True,
            company_owner=self.current_company
        )

        self.adv3 = Internship_ad.objects.create(
            created_at=datetime.now(),
            modified_at=datetime.now(),
            title='Test Ad3',
            city='Sofia',
            field='Information Technology',
            employment_type='Full-Time',
            duration='1 month',
            description='asdhadhakljdh',
            is_active=False,
            company_owner=self.current_company
        )
        self.company_profile_url = reverse('company profile', args=[self.user_company.id])
        self.company_profile_edit_url = reverse('edit company profile', args=[self.user_company.id])
        self.candidate_profile_url = reverse('candidate profile', args=[self.current_candidate.user_id])
        self.candidate_profile_edit_url = reverse('edit candidate profile', args=[self.current_candidate.user_id])
        self.candidate_profile_delete_url = reverse('delete profile', args=[self.user_candidate.id])
        self.company_profile_delete_url = reverse('delete profile', args=[self.user_company.id])

        '''
        get_company_profile - GET 
        edit_company_profile - GET and POST
        get_candidate_profile - GET
        edit_candidate_profiles - GET and POST
        delete_user Get
        applied_candidates - GET
        '''

    def test_get_company_profile_as_anonymous_user_GET(self):
        response = self.client.get(self.company_profile_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/company_profile.html')

    def test_get_company_profile_with_active_ads_GET(self):
        self.client.force_login(self.user_company)

        response = self.client.get(self.company_profile_url, {
            'info': self.current_company,
            'company_ads_active': self.adv2,
            'company_ads_closed': self.adv3
        })

        company_ads = Internship_ad.objects.filter(company_owner=self.current_company.user_id).filter(title=self.adv2)[
            0]

        self.assertTemplateUsed(response, 'profile/company_profile.html')
        self.assertEqual(company_ads.is_active, True)
        self.assertEqual(company_ads.company_owner, self.current_company)

    def test_get_company_profile_with_closed_ads_GET(self):
        self.client.force_login(self.user_company)

        response = self.client.get(self.company_profile_url)

        company_ads = Internship_ad.objects.filter(company_owner=self.current_company).filter(title='Test Ad3')[0]

        self.assertTemplateUsed(response, 'profile/company_profile.html')
        self.assertEqual(company_ads.is_active, False)
        self.assertEqual(company_ads.company_owner, self.current_company)

    def test_get_company_profile_with_active_and_closed_ads_GET(self):
        self.client.force_login(self.user_company)

        response = self.client.get(self.company_profile_url)

        self.assertTemplateUsed(response, 'profile/company_profile.html')
        self.assertEqual(self.adv3.is_active, False)
        self.assertEqual(self.adv2.is_active, True)
        self.assertEqual(self.adv3.company_owner, self.current_company)
        self.assertEqual(self.adv2.company_owner, self.current_company)

    def test_get_company_profile_with_no_ads_GET(self):
        self.client.force_login(self.user_company)
        self.adv2.delete()
        self.adv3.delete()

        response = self.client.get(self.company_profile_url)
        ads = Internship_ad.objects.filter(company_owner=self.current_company)
        self.assertEqual(len(ads), 0)
        self.assertTemplateUsed(response, 'profile/company_profile.html')

    def test_edit_company_profile_change_Name_POST(self):
        self.client.force_login(self.user_company)

        response = self.client.post(self.company_profile_edit_url,
                                    {'company_name': 'New Name', 'email': 'Google@gmail.com', 'company_logo': '',
                                     'description': '', 'company_website': '', 'company_address': '',
                                     'company_phone': '', 'is_complete': False, 'user': self.user_company
                                     })
        current_company = CompanyProfile.objects.get(user_id=self.user_company.id)

        self.assertEqual(current_company.company_name, 'New Name')

    def test_get_candidate_profile_GET(self):
        self.client.force_login(self.user_candidate)

        response = self.client.get(self.candidate_profile_url)

        self.assertTemplateUsed(response, 'profile/candidate_profile.html')

    def test_edit_candidate_profile_change_first_name_POST(self):
        self.client.force_login(self.user_candidate)

        response = self.client.post(self.candidate_profile_edit_url, {
            'first_name': 'Maria', 'last_name': '', 'email': 'C1@gmail.com', 'CV': '', 'profile_pic': ''})

        current_candidate = CandidateProfile.objects.first()

        self.assertEqual(current_candidate.first_name, 'Maria')

    def test_delete_candidate_user_and_the_profile_Delete_successfully(self):
        self.client.force_login(self.user_candidate)

        response = self.client.delete(self.candidate_profile_delete_url)

        candidates_profiles = CandidateProfile.objects.filter(user_id=self.user_candidate.id)

        self.assertEquals(len(candidates_profiles), 0)

    def test_delete_company_user_and_the_profile_Delete_successfully(self):
        self.client.force_login(self.user_company)

        response = self.client.delete(self.company_profile_delete_url)

        company_profiles = CompanyProfile.objects.filter(user_id=self.user_company.id)

        self.assertEquals(len(company_profiles), 0)

    def test_change_company_name_with_already_existing_company_name(self):
        self.user_company2 = UserModel.objects.create_user(email='Google2@gmail.com', password='Donatelo123!',
                                                           profile='Company')
        self.user_company3 = UserModel.objects.create_user(email='Google3@gmail.com', password='Donatelo123!',
                                                           profile='Company')

        self.company2_profile_edit_url = reverse('edit company profile', args=[self.user_company2.id])
        self.company3_profile_edit_url = reverse('edit company profile', args=[self.user_company3.id])
        self.client.force_login(self.user_company2)

        response = self.client.post(self.company2_profile_edit_url,
                                    {'company_name': 'New Name', 'email': 'Google2@gmail.com', 'company_logo': '',
                                     'description': '', 'company_website': '', 'company_address': '',
                                     'company_phone': '', 'is_complete': False, 'user': self.user_company})

        self.client.force_login(self.user_company3)
        response = self.client.post(self.company3_profile_edit_url,
                                    {'company_name': 'New Name', 'email': 'Google3@gmail.com', 'company_logo': '',
                                     'description': '', 'company_website': '', 'company_address': '',
                                     'company_phone': '', 'is_complete': False, 'user': self.user_company})

        company_profile2 = CompanyProfile.objects.get(user_id=self.user_company2.id)
        company_profile3 = CompanyProfile.objects.get(user_id=self.user_company3.id)

        self.assertNotEqual(company_profile2.company_name, company_profile3.company_name)
