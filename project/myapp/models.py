from django.db import models

class Cards(models.Model):
	title = models.CharField(max_length=20)
	description = models.TextField(max_length=20)
	views = models.IntegerField(default=0)
	logo = models.ImageField(upload_to='images/')

	def __str__(self):
		return self.title
