from django.db import models



class Customer(models.Model):
	name  = models.CharField(max_length=200) 
	logo = models.ImageField()
	discription = models.TextField()
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.name

		