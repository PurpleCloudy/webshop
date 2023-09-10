from django import forms
from . import models


class AuthenticationForm(forms.Form):
    email = forms.EmailField()
    password = forms.PasswordInput()

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = models.UserProfile
        fields = ['name', 'surname', 'age', 'phone_number', 'email', 'password',]
        succes_url = 'homepage.html'
        widgets = {
            'password': forms.widgets.HiddenInput()
        }