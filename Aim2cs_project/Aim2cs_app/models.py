from django.db import models
import os
# Create your models here.

class honam(models.Model):
	category = models.CharField(max_length=20)
	uploadedFile = models.FileField(upload_to="")
	dir_name = models.CharField(max_length=200)
	season = models.CharField(max_length=10)
	weather = models.CharField(max_length=20)
