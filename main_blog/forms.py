from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Article


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='ENTER THE NAME', widget=forms.TextInput({'class': 'login'}))
    password1 = forms.CharField(label='ENTER THE PASSWORD', widget=forms.PasswordInput({'class': 'password'}))
    password2 = forms.CharField(label='ENTER THE PASSWORD ONE MORE TIME',
                                widget=forms.PasswordInput({'class': 'password'})
                                )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='ENTER THE NAME',
                               widget=forms.TextInput({'class': 'login'})
                               )
    password = forms.CharField(label='ENTER THE PASSWORD',
                               widget=forms.PasswordInput({'class': 'password'})
                               )

    class Meta:
        model = User
        fields = ['username', 'password']

