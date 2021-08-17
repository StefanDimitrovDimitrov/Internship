from django import forms
from django.core.exceptions import ValidationError


class BotCatcherFormMixin(forms.Form):
    def __init__(self, *args, **kwargs):
        super(BotCatcherFormMixin, self).__init__(*args, **kwargs)
        self.fields['bot_catcher'] = forms.CharField(
            widget=forms.HiddenInput(),
            required=False,
            validators=[validate_bot_catcher_empty])


def validate_bot_catcher_empty(value):
    if value:
        print('You are a bot')
        raise ValidationError('You are a bot')
