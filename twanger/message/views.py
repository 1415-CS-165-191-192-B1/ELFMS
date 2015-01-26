"""See twanger/site/views.py for documentation on the below.
"""


from django.views import generic
from django.http import HttpResponseRedirect

from twanger.message.forms import MessageForm
from twanger.message.models import Message


class MessagePostView(generic.FormView):
    form_class = MessageForm

    def get_success_url(self):
        return '/'

    def form_valid(self, form):
        form_data = form.cleaned_data
        user = self.request.user
        content = form_data['content']
        new_message = Message(content=content, owner=user)
        new_message.save()
        return HttpResponseRedirect(self.get_success_url())