from django.urls import path

from Internship.internship_app.views import catalog_companies, catalog_ad, create_ad, details_ad, edit_ad, \
    delete_ad, apply, deactivate_ad, activate_ad, Home, about

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/',about, name='about'),
    path('companies/', catalog_companies, name='catalog companies'),
    path('ads/', catalog_ad, name='catalog ads'),
    path('create/', create_ad, name='create ad'),
    path('details/<int:pk>', details_ad, name='details ad'),
    path('edit/<int:pk>', edit_ad, name='edit ad'),
    path('delete/<int:pk>', delete_ad, name='delete ad'),
    path('deactivate/<int:pk>', deactivate_ad, name='deactivate ad'),
    path('activate/<int:pk>', activate_ad, name='activate ad'),
    path('apply/<int:pk>', apply, name='apply'),

]