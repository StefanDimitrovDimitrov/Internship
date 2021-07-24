from django.urls import path

from Internship.internship_profiles.views import get_company_details, edit_company_details, \
    get_candidate_details, edit_candidate_details, delete_candidate_details, delete_company_details, \
    change_company_credentials, change_candidate_credentials

urlpatterns = [

    path('companyProfile/<int:pk>', get_company_details, name='details company'),
    path('editCompanyProfile/<int:pk>', edit_company_details, name='edit company'),
    path('changeCompanyCredentials/<int:pk>', change_company_credentials, name='change company credentials'),

    path('deleteCompanyProfile/<int:pk>', delete_company_details, name='delete company'),
    path('candidateProfile/<int:pk>', get_candidate_details, name='details candidate'),
    path('editCandidateProfile/<int:pk>', edit_candidate_details, name='edit candidate profile'),
    path('changeCandidateCredentials/<int:pk>', change_candidate_credentials, name='change candidate credentials'),

    path('deleteCandidateProfile/<int:pk>', delete_candidate_details, name='delete candidate'),
]


import Internship.internship_profiles.signals