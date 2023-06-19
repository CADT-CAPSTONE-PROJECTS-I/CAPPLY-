from django import forms
from .models import Scholarship
from django.contrib.auth.models import User

class ScholarshipForm(forms.ModelForm):
    class Meta:
        model = Scholarship
        fields = ['level', 'school', 'deadline', 'more_info', 'description', 'link_web', 'country']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
            'more_info': forms.Textarea(attrs={'rows': 4}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class EditScholarshipForm(forms.ModelForm):
    class Meta:
        model = Scholarship
        fields = ['level', 'school', 'deadline','more_info','description','link_web','country']
