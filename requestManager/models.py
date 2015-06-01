from django.db import models
from datetime import datetime

# Create your models here.

class resource(models.Model):
    title = models.CharField('Title', max_length=50)
    author = models.CharField('Author', max_length=50)
    edition = models.CharField('Edition', max_length=50)
    subscription_type = models.BooleanField(default=False)
    pub_year = models.IntegerField(default=0)
    price = models.DecimalField('Price', null = True, max_digits = 8, decimal_places = 2)
    creation_date = models.DateTimeField(default=datetime.now)
    approved = models.BooleanField(default=False)
    comment = models.CharField(max_length=200, default='')
    #add foreignkey for model ni user from loginapp
    
    # class Meta:
    #     unique_together = ('title', 'edition',)

    def __unicode__(self):
        return self.title
