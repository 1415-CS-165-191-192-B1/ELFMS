from django import forms

class MessageForm(forms.Form):
    content = forms.CharField(max_length=140, widget=forms.Textarea)
