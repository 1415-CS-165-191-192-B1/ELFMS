from django.contrib import admin

# Register your models here.

from requestmanager.models import requested

# class ToShow(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['name', 'publisher', 'edition','subscription_type']}),
#         ('Comments', {'fields': ['comments'], 'classes': ['collapse']}),
#        ]

admin.site.register(requested)