
# The Django forms module. Used for all form generation and validation
from django import forms


class NewUserForm(forms.Form):
    """A simple form that accepts only the bare needs to create a new user"""
    # A username that's 1-64 characters long
    username = forms.CharField(max_length=64)
    # An email address. Django will validate this for us on the page.
    email = forms.EmailField()
    # A password. This is still just a CharField but we override the widget
    # that the forms module uses to render it so it shows as dots when you
    # type in the <input> on the page.
    password = forms.CharField(widget=forms.PasswordInput)


class LoginForm(forms.Form):
    """A simple form to process a login."""
    username = forms.CharField(max_length=64)
    password = forms.CharField(widget=forms.PasswordInput)
