from django.urls import reverse,resolve
from django.test import SimpleTestCase

from Internship.internship_app.views import Home

'''
path('', Home.as_view(), name='home'),
path('about/', about, name='about'),
path('companies/', CatalogCompanies.as_view(), name='catalog companies'),
path('ads/', catalog_ad, name='catalog ads'),
path('create/', create_ad, name='create ad'),
path('details/<int:pk>', details_ad, name='details ad'),
path('edit/<int:pk>', edit_ad, name='edit ad'),
path('delete/<int:pk>', delete_ad, name='delete ad'),
path('deactivate/<int:pk>', deactivate_ad, name='deactivate ad'),
path('activate/<int:pk>', activate_ad, name='activate ad'),
path('apply/<int:pk>', apply, name='apply'),
'''



class TestUrls(SimpleTestCase):

    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func.view_class,Home)