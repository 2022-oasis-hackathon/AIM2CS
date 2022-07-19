from django.db import models
import os
# Create your models here.

class honam(models.Model):
	category = models.CharField(max_length=20)
	uploadedFile = models.FileField(upload_to="")
	dir_name = models.CharField(max_length=200)
	season = models.CharField(max_length=10, null = True)
	weather = models.CharField(max_length=20, null = True)
	nature = models.CharField(max_length=20, null = True)
	place = models.CharField(max_length=20, null = True)
