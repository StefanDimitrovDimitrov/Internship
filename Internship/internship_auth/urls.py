from django.urls import path

from Internship.internship_auth.views import register_candidate, login_user, logout_user, register_company

urlpatterns = [
    path('register_candidate/', register_candidate, name='register candidate'),
    path('register_company/', register_company, name='register company'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout')
]