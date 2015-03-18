from django.db import models

class requested(models.Model):
    name = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    edition = models.CharField(max_length=50)
    subscription_type = models.BooleanField(default=True)
    Tag= models.IntegerField(default=1)
    comment = models.CharField(max_length=200)
    
    def __unicode__(self):
		return self.name


