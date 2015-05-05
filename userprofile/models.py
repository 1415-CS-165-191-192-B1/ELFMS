from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    number = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    about = models.CharField(max_length=200)
  #   def __unicode__(self):
		# return self.User.name
    
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


