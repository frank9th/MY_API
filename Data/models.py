from django.db import models

# Create your models here.

class Item(models.Model):
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=600)
	price = models.CharField(max_length=20)

	def __str__(self):
		return self.name
		