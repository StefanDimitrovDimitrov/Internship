from django.test import TestCase

from Internship.internship_profiles import CandidateForm

'''

CandidateForm
EditCandidateForm
CompanyForm
EditCompanyForm

'''


class TestFormsProfiles(TestCase):

    def test_candidateForm_with_email_valid(self):
        form = CandidateForm({
            'profile_image': '',
            'email': 'mail@mail.bg',
            'first_name': '',
            'last_name': '',
            'CV':''
        })

        self.assertTrue(form.is_valid())

    def test_candidateForm_no_email_not_valid(self):
        form = CandidateForm({
            'profile_image': '',
            'email': '',
            'first_name': '',
            'last_name': '',
            'CV':''
        })

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)


