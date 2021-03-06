from django import forms

from Internship.common.BootstrapFormMixin import BootstrapFormMixin
from Internship.common.bot_catcher_mixin import BotCatcherFormMixin
from Internship.internship_profiles.models import CompanyProfile, CandidateProfile


class CandidateForm(BootstrapFormMixin, forms.ModelForm, BotCatcherFormMixin):
    class Meta:
        model = CandidateProfile
        fields = ('profile_image','email', 'first_name', 'last_name', 'CV')



class EditCandidateForm(BootstrapFormMixin, forms.ModelForm, BotCatcherFormMixin):
    class Meta:
        model = CandidateProfile
        fields = ('profile_image', 'email', 'first_name', 'last_name', 'CV')


class CompanyForm(BotCatcherFormMixin, BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = CompanyProfile
        fields = '__all__'
        exclude = ('user', 'is_complete')


class EditCompanyForm(CompanyForm):
    class Meta:
        model = CompanyProfile
        fields = ('company_logo', 'company_name','email', 'company_website', 'company_address', 'company_phone', 'description')
        exclude = ('user', 'is_complete',)
