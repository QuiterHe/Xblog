# from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
	author = models.IntegerField()                                 
	title = models.CharField(max_length=200)                       
	text = models.TextField()                                      
	created_data = models.DateTimeField(default=timezone.now)      
	published_data = models.DateTimeField(blank=True, null=True)   

	"""docstring for Post"""
	def publish(self):
		# self.published_data = timezone.now()
		self.published_data = timezone.now()
		self.save()

	def __str__(self):
		return self.title

