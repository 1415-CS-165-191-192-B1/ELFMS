# from django.shortcuts import render
from django.shortcuts import render_to_response
# from django.http import HttpResponse
from django.http import HttpResponseRedirect
# Para magoad ang mga templates per application
# from django.template import RequestContext,loader
# from django.views.generic.base import TemplateView

# for user authentication
from django.contrib import auth
from django.core.context_processors import csrf
from forms import MyRegistrationForm
from django.contrib.formtools.wizard.views import SessionWizardView
from django.core.mail import send_mail
import logging
# Create your views here.
#for login views

def login(request):
    c = {}
    c.update(csrf(request))    
    return render_to_response('login/login.html', c)
    
def auth_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    print username
    print password
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')
   
def loggedin(request):
    return render_to_response('login/loggedin.html', 
                              {'full_name': request.user.username})

def invalid_login(request):
    return render_to_response('login/invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('login/logout.html')

def register_user(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')
        
    else:
        form = MyRegistrationForm()
    args = {}
    args.update(csrf(request))
    
    args['form'] = form
    
    return render_to_response('login/register.html', args)

def register_success(request):
    return render_to_response('login/register_success.html')

class ContactWizard(SessionWizardView):
    template_name = "login/contact_form.html"
    
    def done(self, form_list, **kwargs):
        form_data = process_form_data(form_list)
        
        return render_to_response('login/done.html', {'form_data': form_data})
    
    
def process_form_data(form_list):
    form_data = [form.cleaned_data for form in form_list]
    
    logr.debug(form_data[0]['subject'])
    logr.debug(form_data[1]['sender'])
    logr.debug(form_data[2]['message'])
    
    send_mail(form_data[0]['subject'], 
              form_data[2]['message'], form_data[1]['sender'],
              ['hibbert.michael@gmail.com'], fail_silently=False)
    
    return form_data
# guide for naming kung saan pupunta
'''
def home(request):
	return render (request, 'login/home.html')

def hello(request):

	name="Dyosa"
	html="<html><body> Hi %s. This seems to have worked</body></html>" %name
	return HttpResponse(html)

def hello_template(request):
	name= "Fucker"

	context= {'name':name}
	#Para ma-load si template, tapos ipapasok si context dun kay template	
	return render(request, 'login/logintemplate.html', context)
	
# no need for context uses render_to_response
def hello_template_simple(request):
	name= "CHICHI"
	return render_to_response('login/logintemplate.html', {'name':name})	

class HelloTemplate(TemplateView):

	template_name= 'login/logintemplate.html'

	def get_context_data(self, **kwargs):

		context = super(HelloTemplate,self).get_context_data(**kwargs)
		context['name']= 'Evangeline'
		return context
'''