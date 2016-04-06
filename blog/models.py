from django.db import models
from django.utils import timezone
from django.shortcuts import render


class Post(models.Model):
	author = models.ForeignKey('auth.user')
	
	title = models.CharField(max_length=200)

	text = models.TextField()

	created_date =models.DateTimeField(default=timezone.now)

	published_date = models.DateTimeField(blank=True, null=True)

		
	def published(self):
		self.published_date = timezone.now()
		self.save()

	def _str_(self):
		return self.title

