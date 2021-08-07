from django import forms
from django_summernote.fields import SummernoteTextFormField
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

from Internship.choices.choices import CITY_CHOICES, FIELD_CHOICES, DURATION_CHOICES, EMPLOYMENT_TYPE
from Internship.common.BootstrapFormMixin import BootstrapFormMixin
from Internship.common.bot_catcher_mixin import BotCatcherFormMixin
from Internship.internship_app.models import Internship_ad, AppliedTracking
from Internship.internship_profiles.models import CandidateProfile, CompanyProfile


class AdForm(BootstrapFormMixin, forms.ModelForm, BotCatcherFormMixin):
    class Meta:
        model = Internship_ad
        fields = '__all__'
        widgets = {
            'description': SummernoteWidget(attrs={'class': 'form_control'}),
        }
        exclude = ('user', 'company_owner', 'is_active', 'applied_candidates', 'created_at', 'modified_at')


class ApplyForm(BootstrapFormMixin, forms.ModelForm, BotCatcherFormMixin):
    class Meta:
        model = CandidateProfile
        fields = ('CV',)



class SortForm(forms.Form):
    city = forms.CharField(
        widget=forms.Select(choices=CITY_CHOICES, attrs={'class': 'form-select border rounded-pill'}, ),
    )
    field = forms.CharField(
        widget=forms.Select(choices=FIELD_CHOICES, attrs={'class': 'form-select border rounded-pill'}, ),
    )
    duration = forms.CharField(
        widget=forms.Select(choices=DURATION_CHOICES, attrs={'class': 'form-select border rounded-pill'}, ),
    )
    employment_type = forms.CharField(
        widget=forms.Select(choices=EMPLOYMENT_TYPE, attrs={'class': 'form-select border rounded-pill'}, ),
    )


class SearchForm(forms.Form):
    text = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput
        (attrs={'class': 'form-control border rounded-pill'}))
