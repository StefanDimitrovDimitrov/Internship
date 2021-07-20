from django.urls import path

from Internship.internship_app.views import home, catalog_companies, catalog_ad, create_ad, details_ad, edit_ad, \
    delete_ad, apply

urlpatterns = [
    path('', home, name='home'),
    path('companies/', catalog_companies, name='catalog companies'),
    path('ads/', catalog_ad, name='catalog ads'),
    path('create/', create_ad, name='create ad'),
    path('details/<int:pk>', details_ad, name='details ad'),
    path('edit/<int:pk>', edit_ad, name='edit ad'),
    path('delete/<int:pk>', delete_ad, name='delete ad'),
    path('apply/<int:pk>', apply, name='apply'),
]