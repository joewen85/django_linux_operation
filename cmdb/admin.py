from django.contrib import admin
from .models import Information 

class InformationAdmin(admin.ModelAdmin):
    list_display = ('name','privateip','publicip','use','zoneid','cpu','memory','datadisk')
    
admin.site.register(Information,InformationAdmin)

