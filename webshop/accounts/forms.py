from django import forms


# class AuthenticationForm(forms.Form):
#     email = forms.EmailField()
#     password = forms.CharField(max_length=20, widget=forms.widgets.PasswordInput)

# class RegistrationForm(forms.ModelForm):
#     class Meta:
#         model = models.UserProfile
#         fields = ['name', 'surname', 'age', 'phone_number', 'email', 'password']
#         widgets = {
#             'password': forms.widgets.PasswordInput()
#         }

# class ChangeDetailForm(forms.ModelForm):
#     class Meta:
#         model = models.UserProfile
#         fields = ['name', 'surname', 'age', 'phone_number']

# class PasswordResetForm(forms.Form):
#     email = forms.EmailField()
        
class PasswordResetDoneForm(forms.Form):
    password = forms.CharField(max_length=30, widget=forms.widgets.PasswordInput)
    password_confirm = forms.CharField(max_length=30, widget=forms.widgets.PasswordInput)