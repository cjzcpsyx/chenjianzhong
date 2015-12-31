from django.contrib import admin
from django import forms
from .models import Project, Experience

class CustomExperienceChoiceField(forms.ModelChoiceField):
	def label_from_instance(self, obj):
		return "%s, %s" % (obj.title, obj.role)

class ProjectAdminForm(forms.ModelForm):
	experience = CustomExperienceChoiceField(queryset=Experience.objects.all())
	class Meta:
		model = Experience
		fields = '__all__'

class ProjectAdmin(admin.ModelAdmin):
	list_display = ['name', 'added', 'updated']
	form = ProjectAdminForm


class ExperienceAdmin(admin.ModelAdmin):
	list_display = ['title', 'added', 'updated']

admin.site.register(Project, ProjectAdmin)
admin.site.register(Experience, ExperienceAdmin)