from django import forms

from Internship.internship_app.models import Internship_ad


class AdForm(forms.ModelForm):
    class Meta:
        model = Internship_ad
        fields = '__all__'

