from django.db import models

# Create your models here.

class login(models.Model):
	name = models.CharField(max_length=200)
	job_type = models.IntegerField()
	password = models.CharField(max_length= 200)

	def __unicode__(self):
		return self.name