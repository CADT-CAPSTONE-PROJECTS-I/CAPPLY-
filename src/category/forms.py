from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserChangeForm

class EditProfileForm(UserChangeForm):
    first_name = forms.CharField(max_length=125, widget= forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=125, widget= forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=125, widget= forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'last_name', 'first_name']
    

from django.contrib.auth.forms import PasswordChangeForm
from django import forms

class CustomPasswordChangeForm(PasswordChangeForm):
    new_field = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    old_password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super(CustomPasswordChangeForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].label = "Old Password"

    def clean(self):
        cleaned_data = super(CustomPasswordChangeForm, self).clean()
        # Add any additional form validation or cleaning logic if needed
        return cleaned_data