from django.shortcuts import render
# from django.shortcuts import render
from django.shortcuts import render_to_response
# from django.http import HttpResponse
from django.http import HttpResponseRedirect
# Para magoad ang mga templates per application

from django.core.context_processors import csrf

from forms import MyRequestForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required

# def view_request(request):
  

def create_request(request):
    #return render(request,'requestmanager/request.html')

    if request.method == 'POST':
        form = MyRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/request_success/')
        
    else:
        form = MyRequestForm()
   	args = {}
   	args.update(csrf(request))
    
   	args['form'] = form
    return render_to_response('requestmanager/request.html', args)

def request_success(request):
    return render_to_response('requestmanager/request_success.html')

# def creates(request):
# 	name = request.POST['name']
#     password = request.POST['password']	
#     publisher
#     subscription

# def view_request(request):
#     name = request.POST['name']
#     password = request.POST['password']
#     user = auth.authenticate(username=username, password=password)
#     print username
#     print password
#     if user is not None:
#         auth.login(request, user)
#         return HttpResponseRedirect('/accounts/loggedin')
#     else:
#         return HttpResponseRedirect('/accounts/invalid')
