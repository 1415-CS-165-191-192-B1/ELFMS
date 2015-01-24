from django import template

from twanger.message.models import Message


register = template.Library()

@register.inclusion_tag('message/message_detail.html')
def render_message(message):
    return {'message': message}


@register.inclusion_tag('message/newest_tag.html')
def newest_messages(count):
    messages = Message.objects.all().order_by('-when')
    return {'messages': messages[:count]}

