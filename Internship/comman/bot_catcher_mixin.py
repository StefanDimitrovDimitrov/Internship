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

#
# class DeleteNoteForm(NoteForm, BotChatcherFormMixin):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         BotChatcherFormMixin.__init__(self)
#
#
#     bots_catcher = forms.CharField(
#         widget=forms.HiddenInput(),
#         required=False,
#         validators=[
#             # validate_bot_catcher_empty,
#         ]
#     )
#
#     def clean_bots_catcher(self):
#         value = self.cleaned_data['bots_catcher']
#         validate_bot_catcher_empty(value)
#
#
# def validate_dot(value_to_validate):
#     if '.' in value_to_validate:
#         raise forms.ValidationError('\'.\' is present in value')
#
#
