from django.urls import path

from Internship.internship_profiles.views import get_company_profile, edit_company_profile, \
    get_candidate_profile, edit_candidate_profiles, delete_user, applied_candidates

urlpatterns = [

    path('companyProfile/<int:pk>', get_company_profile, name='company profile'),
    path('editCompanyProfile/<int:pk>', edit_company_profile, name='edit company profile'),
    path('applied_candidates/<int:pk>', applied_candidates, name='applied candidates'),

    path('candidateProfile/<int:pk>', get_candidate_profile, name='candidate profile'),
    path('editCandidateProfile/<int:pk>', edit_candidate_profiles, name='edit candidate profile'),

    path('deleteProfile/<int:pk>', delete_user, name='delete profile')
]
