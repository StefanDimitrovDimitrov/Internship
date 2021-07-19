from django.urls import path

from Internship.internship_app.views import home, catalog, catalog_ad, create_ad

urlpatterns = [
    path('', home, name='home'),
    path('catalog/', catalog, name='catalog'),
    path('catalog_ad/', catalog_ad, name='catalog ads'),
    path('create/', create_ad, name='create ad'),
]