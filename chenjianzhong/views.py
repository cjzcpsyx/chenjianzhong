from django.http import HttpResponse
from django.shortcuts import render
from .models import Experience

def index(request):
	return render(request, 'index.html')

def experiences(request):
	experience_list = Experience.objects.all
	return render(request, 'experiences.html', {'experience_list': experience_list})

def projects(request):
	experience_list = Experience.objects.all
	return render(request, 'experiences.html', {'experience_list': experience_list})