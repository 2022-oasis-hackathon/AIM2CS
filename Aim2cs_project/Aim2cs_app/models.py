from django.db import models
import os
# Create your models here.

class users(models.Model):
	username = models.CharField(max_length=20, primary_key= True)
	userpasswd = models.CharField(max_length=30)

class honam(models.Model):
	username = models.ForeignKey(users, on_delete=models.CASCADE)
	category = models.CharField(max_length=20)
	uploadedFile = models.FileField(upload_to="")
	dir_name = models.CharField(max_length=200)
	season = models.CharField(max_length=10, null = True)
	weather = models.CharField(max_length=20, null = True)
	nature = models.CharField(max_length=20, null = True)
	place = models.CharField(max_length=20, null = True)
	big_area = models.CharField(max_length=20, null = True)
	small_area = models.CharField(max_length=20, null = True)
	detail_area = models.TextField()
	explanation = models.TextField()
	likenum = models.IntegerField(default=0)