from django.http import HttpResponse
from django.shortcuts import render
from .models import Experience, Project

def index(request):
	return render(request, 'index.html')

def experiences(request):
	experience_list = Experience.objects.all
	return render(request, 'experiences.html', {'experience_list': experience_list})

def projects(request):
	project_list = Project.objects.all
	return render(request, 'projects.html', {'project_list': project_list})

def yearbook(request, year):
	return render(request, year + '.html')