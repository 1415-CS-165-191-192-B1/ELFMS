from django import template

from twanger.message.models import Message
from twanger.message.forms import MessageForm

register = template.Library()

@register.inclusion_tag('message/message_detail.html')
def render_message(message):
    return {'message': message}

@register.inclusion_tag('message/message_form.html')
def render_message_form():
    return {'message_form': MessageForm()}

@register.inclusion_tag('message/newest_tag.html')
def newest_messages(count):
    messages = Message.objects.all().order_by('-when')
    return {'messages': messages[:count]}

