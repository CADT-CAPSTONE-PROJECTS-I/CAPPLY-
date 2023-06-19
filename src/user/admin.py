from django.contrib import admin
from .models import Comment, Reply, Profile, ModeratorRequest

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'scholarship', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('user', 'content', 'scholarship')
    list_display_links = ('user', 'content', 'scholarship')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('user', 'content')
    list_display_links = ('user', 'content')
    actions = ['approve_reply']

    def approve_reply(self, request, queryset):
        queryset.update(active=True)
 
 

@admin.register(ModeratorRequest)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'created_on')
    list_filter = ('user', 'created_on')
    search_fields = ('user', 'message')
    list_display_links = ('user', 'message')
 
       
# favorite 
from .models import FavoriteScholarship
admin.site.register(FavoriteScholarship)

# end of favorite

admin.site.register(Profile)

