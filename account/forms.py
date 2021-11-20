from django import forms
from django.contrib.auth import load_backend
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import fields
from django.forms import widgets
from django.forms.widgets import ClearableFileInput, PasswordInput
from django.http.request import RawPostDataException

from account.models import Profile

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=PasswordInput)
    password2 = forms.CharField(label="Repeat Password", widget=PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']


    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise ValidationError("Password Don\'t match")
        return cd['password2']

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

class UserEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')