from django.contrib import admin
from .models import  Country, Scholarship, Profile, Comment, Reply
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    search_fields =['id','name'] 
    list_display_links = ('id','name')

class ScholarshipAdmin(admin.ModelAdmin):
    list_display = ('id','level', 'school', 'deadline','more_info', 'country')
    search_fields =['id','level', 'school', 'deadline','more_info', 'country'] 
    list_display_links = ('id','level', 'school', 'deadline','more_info', 'country')
    prepopulated_fields = {"slug": ("school","level")}
    
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
        
# favorite 
from .models import FavoriteScholarship
admin.site.register(FavoriteScholarship)
# end of favorite

admin.site.register(Country, CountryAdmin)
admin.site.register(Scholarship, ScholarshipAdmin)
admin.site.register(Profile)