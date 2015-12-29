from django.contrib import admin
from .models import Project, Experience

class ProjectAdmin(admin.ModelAdmin):
	list_display = ['name', 'added', 'updated']

class ExperienceAdmin(admin.ModelAdmin):
	list_display = ['title', 'added', 'updated']

admin.site.register(Project, ProjectAdmin)
admin.site.register(Experience, ExperienceAdmin)