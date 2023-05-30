from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserChangeForm

class EditProfileForm(UserChangeForm):
    first_name = forms.CharField(max_length=125, widget= forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=125, widget= forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=125, widget= forms.TextInput(attrs={'class': 'form-control'})

    class Meta:
        model = User
        fields = ['username', 'last_name', 'first_name']
