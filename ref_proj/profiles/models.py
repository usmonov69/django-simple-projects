from django.db import models
from .utils import generator_ref_code
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField(blank=True)
	code = models.CharField(max_length=12, blank=True) 
	recommened_by = models.ForeignKey(User, on_delete=models.CASCADE ,  blank=True, null=True , related_name='ref_by')
	update = models.DateTimeField(auto_now=True)
	create = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return str(f"{self.user.username}-{self.code}")


	def get_recommened_profiles(self):
		qs = Profile.objects.all()
		my_recs= [q for q in qs if q.recommened_by == self.user]
		return my_recs

	def save(self, *args, **kwargs):
		if self.code == "":
			code = generator_ref_code()
			self.code = code
		super().save(*args, **kwargs)