from django.contrib import admin
from .models import Profile , ModeratorRequest
from django.contrib import admin
from django.contrib.auth.models import Group, Permission
from .models import ModeratorRequest
class ModeratorRequestAdmin(admin.ModelAdmin):
    # Register your other admin options for ModeratorRequest model
    pass
    

admin.site.register(ModeratorRequest, ModeratorRequestAdmin)
admin.site.register(Profile)

