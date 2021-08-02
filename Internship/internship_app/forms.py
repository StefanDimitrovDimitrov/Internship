from django import forms
from django_summernote.fields import SummernoteTextFormField
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

from Internship.choices.choices import CITY_CHOICES, FIELD_CHOICES, DURATION_CHOICES, EMPLOYMENT_TYPE
from Internship.internship_app.models import Internship_ad, AppliedTracking
from Internship.internship_profiles.models import CandidateProfile, CompanyProfile


class AdForm(forms.ModelForm):
    class Meta:
        model = Internship_ad
        fields = '__all__'
        widgets = {
             'description': SummernoteWidget(),
            #'description': SummernoteInplaceWidget(),
        }
        exclude = ('user', 'company_owner', 'is_active', 'applied_candidates','created_at','modified_at')


class ApplyForm(forms.ModelForm):
    class Meta:
        model = CandidateProfile
        fields = ('CV',)


class SortForm(forms.Form):
    city = forms.ChoiceField(choices=CITY_CHOICES)
    field = forms.ChoiceField(choices=FIELD_CHOICES)
    duration = forms.ChoiceField(choices=DURATION_CHOICES)
    employment_type = forms.ChoiceField(choices=EMPLOYMENT_TYPE)



class SearchForm(forms.Form):
    text = forms.CharField(max_length=15,required=False)