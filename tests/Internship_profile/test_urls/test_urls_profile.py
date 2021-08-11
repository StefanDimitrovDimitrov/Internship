from django.urls import reverse,resolve
from django.test import SimpleTestCase

from Internship.internship_profiles.views import get_company_profile, edit_company_profile, applied_candidates, \
    get_candidate_profile, delete_user, edit_candidate_profiles

'''

    path('companyProfile/<int:pk>', get_company_profile, name='company profile'),
    path('editCompanyProfile/<int:pk>', edit_company_profile, name='edit company profile'),
    path('applied_candidates/<int:pk>', applied_candidates, name='applied candidates'),


    path('candidateProfile/<int:pk>', get_candidate_profile, name='candidate profile'),
    path('editCandidateProfile/<int:pk>', edit_candidate_profiles, name='edit candidate profile'),

    path('deleteProfile/<int:pk>',delete_user, name='delete profile')
'''

class TestUrlsProfiles(SimpleTestCase):

    def test_getCompanyProfile_url_resolves(self):
        url = reverse('company profile', args=[1])
        self.assertEquals(resolve(url).func, get_company_profile)

    def test_editCompanyProfile_url_resolves(self):
        url = reverse('edit company profile', args=[1])
        self.assertEquals(resolve(url).func, edit_company_profile)

    def test_applied_candidates_url_resolves(self):
        url = reverse('candidate profile', args=[1])
        self.assertEquals(resolve(url).func, get_candidate_profile)

    def test_getCandidateProfile_url_resolves(self):
        url = reverse('applied candidates', args=[1])
        self.assertEquals(resolve(url).func, applied_candidates)

    def test_editCandidateProfile_url_resolves(self):
        url = reverse('edit candidate profile', args=[1])
        self.assertEquals(resolve(url).func, edit_candidate_profiles)

    def test_deleteProfile_url_resolves(self):
        url = reverse('delete profile', args=[1])
        self.assertEquals(resolve(url).func, delete_user)
