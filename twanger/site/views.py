"""The base site views for twanger."""

# Needed for .TemplateView and .FormView
from django.views import generic

# The reverse method allows us to get a url from the string we used for
# name keyword argument in each url pattern in urls.py
from django.core.urlresolvers import reverse

# A base HTTP class that implements a HTTP 302 redirect call
from django.http import HttpResponseRedirect

# authenticate, login, and logout are helper methods provided by contrib.auth
# that operate on User objects from the same module
from django.contrib.auth import authenticate, login, logout

# Django's base user model.
from django.contrib.auth.models import User

# Our new user and login forms we made in forms.py
from twanger.site.forms import NewUserForm, LoginForm


class HomeView(generic.TemplateView):
    """Our view for `/` or `home`. Just a simple template view that points
    to the template ./twanger/site/templates/site/home.html
    """
    template_name = 'site/home.html'


class NewUserSuccessView(generic.TemplateView):
    """A simple template view for a landing page after successful creation
    of a new user.
    """
    template_name = 'site/new_user_success.html'


class NewUserPostView(generic.FormView):
    """A more complicated view using Django's generic FormView. The FormViews
    need a Form class to validate the request object with. If the form passes
    validation it is passed to self.form_valid so you can do what you want with
    the data you collected
    """

    # The Form class to use for validation
    form_class = NewUserForm

    # The template this form is rendered on. This allows the page to be
    # re-rendered on validation errors with helpful messages.
    template_name = 'site/new_user.html'

    def get_success_url(self):
        """Returns a url to redirect the user to if form_valid completes without
        errors.
        """
        return reverse('new-user-success')

    def get_context_data(self, **kwargs):
        """A hook for the base get_context_data so we can add our form to
        the page so it can be rendered in the template.
        """
        context = super(NewUserPostView, self).get_context_data()
        context['new_user_form'] = NewUserForm()
        return context

    def form_valid(self, form):
        """The form has passed validation. This method is passed a copy of
        that form and its data. We use the cleaned data to create the user
        and save it to the database. We then Redirect the user to our defined
        get_success_url.
        """
        form_data = form.cleaned_data
        username = form_data['username']
        password = form_data['password']
        email = form_data['email']
        new_user = User.objects.create_user(username, email, password)
        new_user.save()
        return HttpResponseRedirect(self.get_success_url())


class LoginPostView(generic.FormView):
    """A FormView to handle logging in."""
    form_class = LoginForm
    template_name = 'site/login.html'

    def get_context_data(self, **kwargs):
        """We hook get_context_data so we can provide our form so it can be
        rendered in the page.
        """
        context = super(LoginPostView, self).get_context_data()
        context['login_form'] = LoginForm()
        return context

    def get_success_url(self):
        """We will redirect to our url we named `home` in urls.py"""
        return reverse('home')

    def form_valid(self, form):
        """If the form is valid we will authenticate the user with the
        cleaned_data provided from the form. If the login succeeds and the user
        is_active then we use the login method from contrib.auth to start the
        users session.
        """
        form_data = form.cleaned_data
        user = authenticate(username=form_data['username'],
                            password=form_data['password'])
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return HttpResponseRedirect(self.get_success_url())
        else:
            return self.form_invalid(form)


class LogoutView(generic.TemplateView):
    """A simple template view that tells the user that they are logged out, and
    uses django's logout method from contrib.auth to end the session.
    """
    template_name = 'site/logout_success.html'

    def get_context_data(self, **kwargs):
        context = super(LogoutView, self).get_context_data()
        logout(self.request)
        return context
