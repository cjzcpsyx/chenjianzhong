from django.db import models

class Experience(models.Model):
	company = models.CharField(max_length=200)
	title = models.CharField(max_length=200)
	role = models.CharField(max_length=200)
	description = models.TextField()
	added = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	begin = models.DateTimeField()
	end = models.DateTimeField()
	present = models.BooleanField()

class Project(models.Model):
	name = models.CharField(max_length=200)
	experience = models.ForeignKey(Experience)
	description = models.TextField()
	added = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)