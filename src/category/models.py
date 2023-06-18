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
    slug = models.SlugField(null=False, unique=True, default=slugify(random_slug()))
    
    def get_absolute_url(self):
        return reverse("scholarship_detail", kwargs={"slug": self.slug})
    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(random_slug())
        return super().save(*args, **kwargs)


#profile model
MAJOR_LIST = (
    ('computer science', 'COMPUTER SCIENCE'),
    ('finance', 'FINANCE'),
    ('business administration', 'BUSINESS ADMINISTRATION'),
)

from django.contrib.auth.models import AbstractUser
from django.db import models
import os
from django.contrib.auth.models import AbstractUser, Group, Permission
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, null  =False, on_delete = models.CASCADE)
    profile_pic = models.ImageField(default='images\profile_pics\Default.png', upload_to='images\profile_pics')
    bio = models.TextField(default="This user is lazy and has nothing to say.", max_length=124, null = True, blank = True)

    def __str__(self):
        return str(self.user)
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.profile_pic.path)

        if img.height > 500 or img.width > 500:
            new_img = (500, 500)
            img.thumbnail(new_img)
            img.save(self.profile_pic.path)

def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        
post_save.connect(create_profile, sender=User)

class Comment(models.Model):
    scholarship = models.ForeignKey(Scholarship, on_delete=models.CASCADE, null = False, related_name ='comments')
    user = models.ForeignKey(User, null = False, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    class Meta:
        ordering = ['created_on']
    def __str__(self):
        return 'Comment {} by {}'.format(self.content, self.user)
    
class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    def __str__(self):
        return 'Reply {} by {}'.format(self.content, self.user)
    