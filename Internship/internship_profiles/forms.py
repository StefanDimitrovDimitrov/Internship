from django import forms

from Internship.internship_profiles.models import CompanyProfile, CandidateProfile


class CandidateForm(forms.ModelForm):
    class Meta:
        model = CandidateProfile
        field = '__all__'
        exclude = ('user','email','is_complete')


class CompanyForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        field = '__all__'
        exclude = ('user','email','is_complete')
