from django.db import models

from django.contrib.auth.models import User


class Message(models.Model):
    owner = models.ForeignKey(User, related_name='messages')
    content = models.TextField(max_length=140)
    when = models.DateTimeField(auto_now=True)
