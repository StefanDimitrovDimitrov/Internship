from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from Internship.internship_auth.models import InternshipUser
from Internship.internship_profiles.forms import CompanyForm, CandidateForm
from Internship.internship_profiles.models import CompanyProfile

UserModel = get_user_model()




class RegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email',)

class RegisterFormCompany(CompanyForm, RegisterForm):
    class Meta:
        model = UserModel
        fields = ('company_name','email')


class RegisterFormCandidate(CandidateForm, RegisterForm):
    class Meta:
        model = UserModel
        fields = ('email',)


class LoginForm(forms.Form):
    email = forms.EmailField(
        max_length=30,
    )
    password = forms.CharField(
        max_length=15,
        widget=forms.PasswordInput(),
    )

    def clean_password(self):
        self.user = authenticate(
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
        )

        if not self.user:
            raise ValidationError('Email and/or password incorrect')

    def save(self):
        return self.user


