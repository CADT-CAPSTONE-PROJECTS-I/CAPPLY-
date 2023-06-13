from django.contrib import admin
from .models import  Country, Scholarship, Profile
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    search_fields =['id','name'] 
    list_display_links = ('id','name')

class ScholarshipAdmin(admin.ModelAdmin):
    list_display = ('id','level', 'school', 'deadline','more_info', 'country')
    search_fields =['id','level', 'school', 'deadline','more_info', 'country'] 
    list_display_links = ('id','level', 'school', 'deadline','more_info', 'country')
    prepopulated_fields = {"slug": ("school","level")}

admin.site.register(Country, CountryAdmin)
admin.site.register(Scholarship, ScholarshipAdmin)
admin.site.register(Profile)