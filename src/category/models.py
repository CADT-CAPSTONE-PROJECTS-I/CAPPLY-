from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.urls import reverse
from django.utils.text import slugify
from django.utils.crypto import get_random_string
import random, string
from django.utils import timezone
from django.contrib.auth.models import UserManager
import re
# Create your models here.
def randomString():
    um = UserManager()
    return( um.make_random_password( length=25 ) )

def random_slug():
    allowed_chars = ''.join((string.ascii_letters, string.digits))
    unique_slug = ''.join(random.choice(allowed_chars) for _ in range(32))
    return unique_slug

class Country(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    # continent = models.CharField(max_length=5, choices=CONTINENT)
    def __str__(self):
        return self.name
    

class Scholarship(models.Model):
    id = models.BigAutoField(primary_key=True)
    level = models.CharField(max_length=120)
    school = models.CharField(max_length=200)
    deadline = models.DateField(null=True)
    more_info = models.TextField()
    description = models.TextField(blank=True, null=True, max_length=275)
    link_web = models.CharField(max_length=200)
    country = models.CharField(max_length=120)
    slug = models.SlugField(null=False, unique=True, default=slugify(random_slug))
    
    def get_absolute_url(self):
        return reverse("scholarship_detail", kwargs={"slug": self.slug})
    


#profile model
MAJOR_LIST = (
    ('computer science', 'COMPUTER SCIENCE'),
    ('finance', 'FINANCE'),
    ('business administration', 'BUSINESS ADMINISTRATION'),
)

class Profile(models.Model):
    user = models.OneToOneField(User, null  =True, on_delete = models.CASCADE)
    profile_pic = models.ImageField(default='images\profile_pics\Default.png', upload_to='images\profile_pics')
    bio = models.TextField(default="This user is lazy and has nothing to say.", max_length=124, null = True, blank = True)

    def __str__(self):
        return str(self.user)

def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        
post_save.connect(create_profile, sender=User)
