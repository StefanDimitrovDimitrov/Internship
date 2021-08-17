from django.test import SimpleTestCase

from Internship.internship_app import AdForm, ApplyForm


class TestForms(SimpleTestCase):

    def test_ad_form_valid_data(self):
        form = AdForm(data={
            'title': 'AdTitle',
            'city': 'Sofia',
            'field': 'Information Technology',
            'employment_type': 'Full-Time',
            'duration': '1 month',
            'description': 'Some Des....',
        })
        self.assertTrue(form.is_valid())

    def test_ad_form_no_data(self):
        form = AdForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 6)

    def test_ad_form_wrong_len_of_field_title(self):
        form = AdForm(data={
            'title': 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend',
            'city': 'Sofia',
            'field': 'Information Technology',
            'employment_type': 'Full-Time',
            'duration': '1 month',
            'description': 'Some Des....',
        })

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_ApplyForm_valid_data(self):

        form = ApplyForm(data={
            'CV': 'intern_cv/fileCV.docx'
        })

        self.assertTrue(form.is_valid())

