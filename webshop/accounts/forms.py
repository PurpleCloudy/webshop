from django import forms
from . import models


class AuthenticationForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=20, widget=forms.widgets.PasswordInput)

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = models.UserProfile
        fields = ['name', 'surname', 'age', 'phone_number', 'email', 'password']
        widgets = {
            'password': forms.widgets.PasswordInput()
        }

class ChangeDetailForm(forms.ModelForm):
    class Meta:
        model = models.UserProfile
        fields = ['name', 'surname', 'age', 'phone_number']