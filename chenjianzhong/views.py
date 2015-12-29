from django.http import HttpResponse
from django.shortcuts import render
from .models import Experience

def index(request):
	return HttpResponse("Hello, World")

def experiences(request):
	experience_list = Experience.objects.all
	return render(request, 'experiences.html', {'experience_list': experience_list})