import django
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
CONTINENT = [
    ("ASIA",'Asia'), 
    ("AFRIC",'Africa'),
    ("NA",'North America'), 
    ("SA",'South America'), 
    ("ANTIC",'Antacitica'), 
    ("EURO",'Europe'), 
    ("AUS",'Australia'),
]

# class continent(models.Model):
#     # id = models.BigAutoField(primary_key=True)
#     code = models.CharField(max_length=10, primary_key=True)
#     code = models.CharField(max_length=10, primary_key=True)
#     name = models.CharField(max_length=255)
#     description= models.TextField()

#     def __str__(self):
#         return self.name 
    
class Country(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    continent = models.CharField(max_length=5, choices=CONTINENT)
    def __str__(self):
        return self.name
    

class Scholarship(models.Model):
    id = models.BigAutoField(primary_key=True)
    level = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    deadline = models.DateField()
    more_info = models.TextField()
    description = models.TextField(blank=True, null=True, max_length=275)
    link_web = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    def __str__(self):
        return self.school 
    
    # file = models.FileField(upload_to="documents/%Y/%m/%d", validators=[validate_file_extension])
    
    
#profile model
MAJOR_LIST = (
    ('computer science', 'COMPUTER SCIENCE'),
    ('finance', 'FINANCE'),
    ('business administration', 'BUSINESS ADMINISTRATION'),
)

class Profile(models.Model):
    user = models.OneToOneField(User, null  =True, on_delete = models.CASCADE)
    profile_pic = models.ImageField(default='static\images\profile_pics\Default.png', upload_to='static\images\profile_pics')
    bio = models.TextField(default="This user is lazy and has nothing to say.", max_length=124, null = True, blank = True)
    school = models.TextField(max_length=30, null = True, blank = True)
    phone = models.TextField(max_length=10, null = True, blank = True)
    major = models.CharField(max_length=40, choices=MAJOR_LIST, default='N/A', null = True, blank = True)

    def __str__(self):
        return f'{self.user.username} Profile'
