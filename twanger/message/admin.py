# admin is the main module for django's included admin interface.
from django.contrib import admin

# Import our Message model from twanger/message/models.py
from models import Message


class MessageAdmin(admin.ModelAdmin):
    """Django's ModelAdmin classed allow you to specify how and which fields
    appear in the admin page.
    """
    # Override the default columns in the list display page.
    list_display = ('when', 'owner', 'content')

# register the model and the ModelAdmin class with the admin site so it
# will be included when you log in.
admin.site.register(Message, MessageAdmin)