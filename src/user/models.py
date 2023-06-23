from django.conf import settings
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
    is_email_verified = models.BooleanField(default=False)
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

from django.contrib.auth.models import Group, Permission
STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

# MDOERATOR
class ModeratorRequest(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    # def set_permissions_for_moderator_request(self, user, status):
    #     # Remove existing permissions
    #     user.user_permissions.clear()

    #     if status == 'pending':
    #         # Assign permissions for pending status
    #         # Example: Can view own request
    #         permission_view_own_request = Permission.objects.get(codename='view_own_request')
    #         user.user_permissions.add(permission_view_own_request)
    #     elif status == 'approved':
    #         # Assign permissions for approved status
    #         # Example: Can view all requests
    #         permission_view_all_requests = Permission.objects.get(codename='view_all_requests')
    #         user.user_permissions.add(permission_view_all_requests)
    #     elif status == 'rejected':
    #         # Assign permissions for rejected status
    #         # Example: Can view own request and rejected requests
    #         permission_view_own_request = Permission.objects.get(codename='view_own_request')
    #         permission_view_rejected_requests = Permission.objects.get(codename='view_rejected_requests')
    #         user.user_permissions.add(permission_view_own_request, permission_view_rejected_requests)