from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Profile, UserMtAccounts


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class UserMtAccountsCreation(forms.ModelForm):
    account_name = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter account name', 'id': 'account_name'}))

    class Meta:
        model = UserMtAccounts
        fields = ['account_name']


class InputForm(forms.Form):
    account_login = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter account login', 'id': 'account_login'}))
    account_password = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter account password', 'id': 'account_password'}))
    server_name = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter server name', 'id': 'server_name'}))
