from django.test import TestCase, Client
from django.urls import reverse


class Home(TestCase):

    def test_get_home_page(self):
        self.client = Client()

        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
