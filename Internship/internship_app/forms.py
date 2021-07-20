from django import forms

from Internship.internship_app.models import Internship_ad
from Internship.internship_profiles.models import CandidateProfile


class AdForm(forms.ModelForm):
    class Meta:
        model = Internship_ad
        fields = '__all__'
        exclude = ('user',)


class ApplyForm(forms.ModelForm):
    class Meta:
        model = CandidateProfile
        fields = ('CV',)