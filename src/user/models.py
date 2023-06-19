from django.db import models
from category.models import Scholarship
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.db import models
from PIL import Image

# PROFILE MODEL
# FAVORITED SCHOLARSHIP MODEL
# COMMENT MODEL
# REPLY MODEL

# PROFILE
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

# COMMENT 
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
    
# REPLY
class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    def __str__(self):
        return 'Reply {} by {}'.format(self.content, self.user)
    
# FAVORITE
class FavoriteScholarship(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    scholarship_school = models.CharField(max_length=100)
    scholarship_link = models.CharField(max_length=120, null=True)
   
    def __str__(self):
        return self.scholarship_school
   
class Favorited(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    scholarship = models.ForeignKey(Scholarship, on_delete=models.CASCADE, default=1)
    activation = models.BooleanField()


STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

# MDOERATOR
class ModeratorRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')