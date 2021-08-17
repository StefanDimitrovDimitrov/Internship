from django.urls import reverse,resolve
from django.test import SimpleTestCase

from Internship.internship_app.views import Home, about, CatalogCompanies, catalog_ad, create_ad, details_ad, edit_ad, \
    delete_ad, deactivate_ad, activate_ad, apply


class TestUrls(SimpleTestCase):

    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func.view_class,Home)

    def test_about_url_resolves(self):
        url = reverse('about')
        self.assertEquals(resolve(url).func, about)

    def test_catalog_companies_url_resolves(self):
        url = reverse('catalog companies')
        self.assertEquals(resolve(url).func.view_class,CatalogCompanies)

    def test_ads_url_resolves(self):
        url = reverse('catalog ads')
        self.assertEquals(resolve(url).func, catalog_ad)

    def test_create_ad_url_resolves(self):
        url = reverse('create ad')
        self.assertEquals(resolve(url).func, create_ad)

    def test_details_ad_url_resolves(self):
        url = reverse('details ad', args=[1])
        self.assertEquals(resolve(url).func,details_ad)

    def test_edit_ad_url_resolves(self):
        url = reverse('edit ad', args=[1])
        self.assertEquals(resolve(url).func,edit_ad)

    def test_delete_ad_url_resolves(self):
        url = reverse('delete ad', args=[1])
        self.assertEquals(resolve(url).func,delete_ad)

    def test_deactivate_ad_url_resolves(self):
        url = reverse('deactivate ad', args=[1])
        self.assertEquals(resolve(url).func,deactivate_ad)

    def test_activate_ad_url_resolves(self):
        url = reverse('activate ad', args=[1])
        self.assertEquals(resolve(url).func,activate_ad)

    def test_apply_ad_url_resolves(self):
        url = reverse('apply', args=[1])
        self.assertEquals(resolve(url).func,apply)