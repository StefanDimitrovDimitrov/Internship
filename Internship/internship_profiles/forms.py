from django import forms

from Internship.internship_profiles.models import CompanyProfile, CandidateProfile


class CandidateForm(forms.ModelForm):
    class Meta:
        model = CandidateProfile
        fields = '__all__'
        exclude = ('user', 'email', 'is_complete')


class EditCandidateForm(CandidateForm):
    pass


class CompanyForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        fields = '__all__'
        exclude = ('user', 'email', 'is_complete')


class EditCompanyForm(CompanyForm):
    class Meta:
        model = CompanyProfile
        fields = '__all__'
        exclude = ('user', 'email', 'is_complete',)
