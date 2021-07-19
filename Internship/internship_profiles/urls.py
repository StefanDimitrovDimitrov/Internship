from django.urls import path

from Internship.internship_profiles.views import get_company_profile, edit_company_profile, delete_company_profile, \
    get_candidate_details, edit_candidate_details, delete_candidate_details

urlpatterns = [

    path('companyProfile/<int:pk>', get_company_profile, name='company details'),
    path('companyProfile/', edit_company_profile, name='company details'),
    path('companyProfile/', delete_company_profile, name='company details'),
    path('companyProfile/', get_candidate_details, name='company details'),
    path('companyProfile/', edit_candidate_details, name='company details'),
    path('companyProfile/', delete_candidate_details, name='company details'),
]