from django import forms
from demoapp import app_settings
from django.utils.translation import ugettext_lazy as _


class DemoLoginForm(forms.Form):
    password = forms.CharField(label=_('Password'), widget=forms.PasswordInput)

    def clean_password(self):
        password = self.cleaned_data['password']
        if password != app_settings.ACCESS_PASSWORD:
            raise forms.ValidationError(_('Incorrect password'))
        return password
