from django.db import models
from datetime import datetime

# Create your models here.

class resource(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    edition = models.CharField(max_length=50)
    subscription_type = models.BooleanField(default=True)
    pub_year = models.IntegerField(default=0)
    creation_date = models.DateTimeField(default=datetime.now)
    tag= models.IntegerField(default=1)
    comment = models.CharField(max_length=200)
    #add foreignkey for model ni user from loginapp
    
    def __unicode__(self):
        return self.title

