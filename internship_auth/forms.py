from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from Internship.common.BootstrapFormMixin import BootstrapFormMixin
from Internship.common.bot_catcher_mixin import BotCatcherFormMixin
from Internship.internship_auth.models import InternshipUser
from Internship.internship_profiles.forms import CompanyForm, CandidateForm
from Internship.internship_profiles.models import CompanyProfile

UserModel = get_user_model()


class RegisterForm(BootstrapFormMixin, UserCreationForm, BotCatcherFormMixin):
    class Meta:
        model = UserModel
        fields = ('email',)

class ChangePassword(BootstrapFormMixin, PasswordChangeForm):
    pass

class LoginForm(forms.Form):
    email = forms.EmailField(
        max_length=30,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        max_length=15,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_password(self):
        self.user = authenticate(
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
        )

        if not self.user:
            raise ValidationError('Email and/or password incorrect')

    def save(self):
        return self.user
