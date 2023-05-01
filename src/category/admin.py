from django.contrib import admin
from .models import  Country, Scholarship

class ContinentAdmin(admin.ModelAdmin):
    pass

# Register your models here.
# admin.site.register(continent, )
admin.site.register(Country)
admin.site.register(Scholarship)