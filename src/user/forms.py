from django import forms
from django.contrib.auth.models import User
from .models import Profile, ModeratorRequest


class EditUserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=125, widget= forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=125, widget= forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=125, widget= forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ['username', 'last_name', 'first_name']
          
class EditProfileForm(forms.ModelForm):
    profile_pic = forms.ImageField()
    bio = forms.Textarea()
    class Meta:
        model = Profile
        fields = ['profile_pic', 'bio']
        widget= {
            'profile_pic' : forms.TextInput(attrs={'class': 'form-control'}),
            'bio' : forms.TextInput(attrs={'class': 'form-control'})
        }


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
        return cleaned_data
    
    
    

class MyForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Message', widget=forms.Textarea)
    image = forms.ImageField(label='image')
    
class CVForm(forms.Form):
    # Personal Information
    full_name = forms.CharField(label='Full Name', max_length=100)
    email = forms.EmailField(label='Email')
    phone_number = forms.CharField(label='Phone Number', max_length=20, required=False)
    address = forms.CharField(label='Address', max_length=200, required=False)

    # Professional Summary/Objective
    summary = forms.CharField(label='Professional Summary', widget=forms.Textarea)

    # Education
    institution_name = forms.CharField(label='Institution Name', max_length=100)
    degree_earned = forms.CharField(label='Degree Earned', max_length=100)
    field_of_study = forms.CharField(label='Field of Study', max_length=100)
    dates_of_attendance = forms.CharField(label='Dates of Attendance', max_length=100)

    # Experience
    company_name = forms.CharField(label='Company Name', max_length=100)
    job_title = forms.CharField(label='Job Title', max_length=100)
    employment_dates = forms.CharField(label='Employment Dates', max_length=100)
    responsibilities = forms.CharField(label='Responsibilities', widget=forms.Textarea)
    achievements = forms.CharField(label='Achievements', widget=forms.Textarea)

    # Skills
    skills = forms.CharField(label='Skills', widget=forms.Textarea, required=False)

    # Certifications and Training
    certifications = forms.CharField(label='Certifications', widget=forms.Textarea, required=False)

    # Projects
    project_name = forms.CharField(label='Project Name', max_length=100 , required=False)
    purpose = forms.CharField(label='Purpose', widget=forms.Textarea, required=False)
    role = forms.CharField(label='Role', max_length=100)
    technologies_used = forms.CharField(label='Technologies Used', max_length=200, required=False)
    outcomes = forms.CharField(label='Outcomes', widget=forms.Textarea, required=False)

    # Awards and Achievements
    awards = forms.CharField(label='Awards', widget=forms.Textarea, required=False)

    # Languages
    languages = forms.CharField(label='Languages', widget=forms.Textarea, required=False)

    # Interests and Hobbies
    interests = forms.CharField(label='Interests and Hobbies', widget=forms.Textarea, required=False)

    # References
    references = forms.CharField(label='References', widget=forms.Textarea, required=False)
    
    image_file = forms.ImageField(label='Image')


from .models import Comment, Reply
from django import forms

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    class Meta:
        model = Comment
        fields = ['content']
        
class ReplyForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    class Meta:
        model = Reply
        fields = ['content']
        
        
class ModeratorRequestForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    class Meta:
        model = ModeratorRequest
        fields = ['message']
        
        
