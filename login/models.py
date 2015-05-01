from django.db import models

# User Roles are only LFC, Dep't Chair, and Librarian
class UserRoles(models.Model):
    user_role = models.CharField(max_length=200)

    def __unicode__(self):
        return self.user_role

class Users(models.Model):
    user_role = models.ForeignKey(UserRoles) 
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __unicode__(self):
        return self.username, self.password

    # def auth(username, password):
    #     self.username = username
    #     self.password = password
    #     return self.username
