from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email", "first_name", "last_name")
        """widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'password1': forms.PasswordInput(attrs={'class':'form-control'}),
            'password2': forms.PasswordInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
        }"""

class FormLogin(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control uk-form-large'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control uk-form-large'}))


class FormRecovery(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control uk-form-large'}))

class FormRedefine(forms.Form):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control uk-form-large'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control uk-form-large'}))