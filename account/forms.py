from django import forms
from django.contrib.auth import load_backend
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import fields
from django.forms.widgets import ClearableFileInput

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegisterationForm(forms.ModelForm):
    password = forms.CharField(label = "Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label= "Repeat Password", widget= forms)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd ['password2']:
            raise ValidationError("Password Don\'t match")
        return cd['password2']

  