from django.contrib import admin
from .models import  Country, Scholarship
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    search_fields =['id','name'] 
    list_display_links = ('id','name')

class ScholarshipAdmin(admin.ModelAdmin):
    list_display = ('id','level', 'school', 'deadline','more_info', 'country')
    search_fields =['id','level', 'school', 'deadline','more_info', 'country'] 
    list_display_links = ('id','level', 'school', 'deadline','more_info', 'country')
    prepopulated_fields = {"slug": ("school","level")}


# @admin.register(ScholarshipEdit)
# class ScholarshipEditAdmin(admin.ModelAdmin):
#     list_display = ('user', 'scholarship', 'updated_on','approved')
#     list_filter = ('approved', 'updated_on')
#     search_fields = ('user', 'scholarship', 'updated_on')
#     list_display_links = ('user', 'scholarship', 'updated_on')
#     actions = ['approve_edit_scholarship']

#     def approve_edit_scholarship(self, request, queryset):
#         queryset.update(approved=True)
        
admin.site.register(Country, CountryAdmin)
admin.site.register(Scholarship, ScholarshipAdmin)