from django.urls import path

from Internship.internship_auth.views import register_candidate, login_user, logout_user, register_company, \
    change_company_credentials, change_candidate_credentials

urlpatterns = [
    path('register_candidate/', register_candidate, name='register candidate'),
    path('register_company/', register_company, name='register company'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('changeCompanyCredentials/<int:pk>', change_company_credentials, name='change company credentials'),
    path('changeCandidateCredentials/<int:pk>', change_candidate_credentials, name='change candidate credentials'),
]