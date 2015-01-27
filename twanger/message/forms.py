from django import forms

class MessageForm(forms.Form):
    """A simple form using a Textarea widget. see twanger/site/forms.py
    for more documentation.
    """
    content = forms.CharField(max_length=140, widget=forms.Textarea)
