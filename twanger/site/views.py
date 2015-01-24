from django.views import generic
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from twanger.site.forms import NewUserForm, LoginForm


class HomeView(generic.TemplateView):
    template_name = 'site/home.html'


class NewUserSuccessView(generic.TemplateView):
    template_name = 'site/new_user_success.html'


class NewUserPostView(generic.FormView):
    form_class = NewUserForm
    template_name = 'site/new_user.html'

    def get_success_url(self):
        return reverse('new-user-success')

    def get_context_data(self, **kwargs):
        context = super(NewUserPostView, self).get_context_data()
        form = NewUserForm()
        context['new_user_form'] = form
        return context

    def form_valid(self, form):
        form_data = form.cleaned_data
        username = form_data['username']
        password = form_data['password']
        email = form_data['email']
        new_user = User.objects.create_user(username, email, password)
        new_user.save()
        return HttpResponseRedirect(self.get_success_url())


class LoginPostView(generic.FormView):
    form_class = LoginForm
    template_name = 'site/login.html'

    def get_context_data(self, **kwargs):
        context = super(LoginPostView, self).get_context_data()
        form = LoginForm()
        context['login_form'] = form
        return context

    def get_success_url(self):
        return reverse('home')

    def form_valid(self, form):
        form_data = form.cleaned_data
        user = authenticate(username=form_data['username'],
                            password=form_data['password'])
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return HttpResponseRedirect(self.get_success_url())
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        """
        If the form is invalid, re-render the context data with the
        data-filled form and errors.
        """
        return self.render_to_response(self.get_context_data(form=form))


class LogoutView(generic.TemplateView):
    template_name = 'site/logout_success.html'

    def get_context_data(self, **kwargs):
        context = super(LogoutView, self).get_context_data()
        logout(self.request)
        return context
