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


class ApplyForm(forms.ModelForm, BotCatcherFormMixin, BootstrapFormMixin):
    class Meta:
        model = CandidateProfile
        fields = ('CV',)


# class SortForm(forms.Form):
#     city = forms.ChoiceField(choices=CITY_CHOICES)
#     field = forms.ChoiceField(choices=FIELD_CHOICES)
#     duration = forms.ChoiceField(choices=DURATION_CHOICES)
#     employment_type = forms.ChoiceField(choices=EMPLOYMENT_TYPE)


class SortForm(forms.Form):
    city = forms.CharField(
        widget=forms.Select(choices=CITY_CHOICES, attrs={'class': 'form-select'}, ),
    )
    field = forms.CharField(
        widget=forms.Select(choices=FIELD_CHOICES, attrs={'class': 'form-select'}, ),
    )
    duration = forms.CharField(
        widget=forms.Select(choices=DURATION_CHOICES, attrs={'class': 'form-select'}, ),
    )
    employment_type = forms.CharField(
        widget=forms.Select(choices=EMPLOYMENT_TYPE, attrs={'class': 'form-select'}, ),
    )


class SearchForm(forms.Form):
    text = forms.CharField(
        max_length=30,
        required=False,
        help_text='Search by company',
        widget=forms.TextInput
        (attrs={'class': 'form_control'}))
