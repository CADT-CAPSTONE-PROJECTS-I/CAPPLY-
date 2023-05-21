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
    link_web = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    def __str__(self):
        return self.school 
    
    # file = models.FileField(upload_to="documents/%Y/%m/%d", validators=[validate_file_extension])


class Profile(models.Model):
    user = models.OneToOneField(User, null  =True, on_delete = models.CASCADE)
    profile = models.ImageField(User, null = True, blank = True, upload_to = r"C:\Project\CAPPLY-\CAPPLY--1\src\template\user\profile_pictures")
    bio = models.TextField(max_length=124, null = True, blank = True)
    school = models.TextField(max_length=30, null = True, blank = True)
    phone = models.TextField(max_length=10, null = True, blank = True)
    major = models.TextField(null = True, blank = True)

    def __str__(self):
        return str(self.user) 
