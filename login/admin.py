from django.contrib import admin

# Register your models here.

from login.models import login

class loginAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'job_type']}),
        ('Password', {'fields': ['password'], 'classes': ['collapse']}),
       ]

admin.site.register(login, loginAdmin)