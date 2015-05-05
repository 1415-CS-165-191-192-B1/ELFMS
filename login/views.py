from login.models import Users
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.context_processors import csrf
 
# Create your views here.

def login(request):
    c = {}
    c.update(csrf(request))    
    return render_to_response('login/login.html', c)


def auth_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = Users.getUser(username=username, password=password)
    print username
    print password
    if user is not None:
        print model.getPassword(username, password)

        return HttpResponseRedirect('/login/loggedin')
    else:
        return HttpResponseRedirect('/login/invalid')

def loggedin(request):
    return render_to_response('login/loggedin.html') 
                              # {'full_name': request.user.username})

def invalid_login(request):
    return render_to_response('login/invalid.html')