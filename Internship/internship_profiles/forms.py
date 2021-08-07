from django import forms

from Internship.common.BootstrapFormMixin import BootstrapFormMixin
from Internship.common.bot_catcher_mixin import BotCatcherFormMixin
from Internship.internship_profiles.models import CompanyProfile, CandidateProfile


class CandidateForm(BootstrapFormMixin,forms.ModelForm,BotCatcherFormMixin):

    class Meta:
        model = CandidateProfile
        fields = ('profile_image','first_name','last_name','CV')
        exclude = ('user', 'email', 'is_complete')


class EditCandidateForm(CandidateForm):
    pass


class CompanyForm(BotCatcherFormMixin,BootstrapFormMixin,forms.ModelForm):

    class Meta:
        model = CompanyProfile
        fields = '__all__'
        exclude = ('user', 'email', 'is_complete')


class EditCompanyForm(CompanyForm):

    class Meta:
        model = CompanyProfile
        fields = ('company_logo','company_name', 'company_website','company_address','company_phone','description')
        exclude = ('user', 'email', 'is_complete',)
