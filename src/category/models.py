import django
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from datetime import datetime
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
    # id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    continent = models.CharField(max_length=5, choices=CONTINENT)
    def __str__(self):
        return self.name
    

class Scholarship(models.Model):
    # id = models.BigAutoField(primary_key=True)
    title = models.CharField("scholarship's title",max_length=255)
    tag = models.CharField(max_length=255)
    date_open = models.DateField()
    date_close = models.DateField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.title 
    
    # file = models.FileField(upload_to="documents/%Y/%m/%d", validators=[validate_file_extension])


    