from django.contrib import admin
from .models import monitors,Experience,question

class monitorAdmin(admin.ModelAdmin):
    list_display = ('servername','item','value','serverip','time')

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title','author','timestamp')

class questionAdmin(admin.ModelAdmin):
    list_display = ('title','author','timestamp')
    
admin.site.register(monitors,monitorAdmin)
admin.site.register(Experience,ExperienceAdmin)
admin.site.register(question,questionAdmin)

