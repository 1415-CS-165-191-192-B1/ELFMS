from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.context_processors import csrf
# Create your views here.

def login(request):
    c = {}
    c.update(csrf(request))    
    return render_to_response('login/login.html', c)
#     c = {}
#     c.update(csrf(request))    
#     return render_to_response('login/login.html', c)
