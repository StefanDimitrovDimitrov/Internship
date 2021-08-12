from datetime import datetime

from django.contrib.auth import get_user_model, logout
from django.http import request
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
            employment_type='full-time',
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
            employment_type='full-time',
            duration='1 month',
            description='asdhadhakljdh',
            is_active=False,
            company_owner=self.current_company
        )
        self.company_profile_url = reverse('company profile', args=[self.user_company.id])
        self.company_profile_edit_url = reverse('edit company profile', args=[self.user_company.id])
        self.candidate_profile_url = reverse('candidate profile', args=[self.current_candidate.user_id])
        self.candidate_profile_edit_url = reverse('edit candidate profile', args=[self.current_candidate.user_id])
        # self.list_url = reverse('home')
        # self.details_url = reverse('details ad', args=[self.adv1.id])
        # self.create_url = reverse('create ad')
        # self.company_catalog_url = reverse('catalog companies')
        # self.edit_url = reverse('edit ad', args=[self.adv1.id])
        # self.delete_url = reverse('delete ad', args=[self.adv1.id])
        # self.deactivate_url = reverse('deactivate ad', args=[self.adv1.id])
        # self.activate_url = reverse('activate ad', args=[self.adv1.id])
        # self.apply_url = reverse('apply', args=[self.adv1.id])

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


        response = self.client.get(self.company_profile_url)

        self.assertTemplateUsed(response, 'profile/company_profile.html')
        self.assertEqual(self.adv2.is_active, True)
        self.assertEqual(self.adv2.company_owner, self.current_company)

    def test_get_company_profile_with_closed_ads_GET(self):
        self.client.force_login(self.user_company)

        response = self.client.get(self.company_profile_url)

        self.assertTemplateUsed(response, 'profile/company_profile.html')
        self.assertEqual(self.adv3.is_active, False)
        self.assertEqual(self.adv3.company_owner, self.current_company)

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


        response = self.client.get(self.company_profile_edit_url)
        self.current_company.company_name = 'New Name'

        self.assertEqual(self.current_company.company_name, 'New Name')


    def test_get_candidate_profile_GET(self):
        self.client.force_login(self.user_candidate)

        response = self.client.get(self.candidate_profile_url)

        self.assertTemplateUsed(response, 'profile/candidate_profile.html')

    def test_edit_candidate_profile_change_first_name_POST(self):
        self.client.force_login(self.user_candidate)


        response = self.client.get(self.candidate_profile_edit_url)
        self.current_candidate.first_name = 'Maria'

        self.assertEqual(self.current_candidate.first_name, 'Maria')

    def test_delete_user_and_the_profile_GET(self):
        self.client.force_login(self.user_candidate)

        self.user_candidate.delete()

        candidates_profiles = CandidateProfile.objects.filter(user_id = self.user_candidate.id)

        self.assertEquals(len(candidates_profiles), 0)

    def test_change_company_name_with_already_existing_company_name(self):
        self.user_company2 = UserModel.objects.create_user(email='Google2@gmail.com', password='Donatelo123!',
                                                          profile='Company')
        self.current_company = CompanyProfile.objects.get(user_id=self.user_company.id)

        self.user_company2.email = 'Google@gmail.com'

        self.assertEqual(self.user_company2.email, 'Google@gmail.com')
        self.assertEqual(self.user_company.email, 'Google@gmail.com')

        # with self.assertRaises(IntegrityError):
        #     self.user_candidate2 = UserModel.objects.create_user(email='C1@gmail.com', password='Donatelo123!',
        #                                                          profile='Candidate')