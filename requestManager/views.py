from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from requestManager.models import resource
from django.template import RequestContext
from requestManager.forms import resourceForm, resourceSearchForm

# Create your views here.
def reqManager(request):
    latest_request = resource.objects.order_by('-creation_date')[:10]
    context = {'latest_request': latest_request}
    return render(request, 'requestManager/index.html', context)
    
def detail(request, resource_id):
    r = get_object_or_404(resource, pk=resource_id)
    return render(request, 'requestManager/detail.html', {'r': r})

def createRequest(request):
	if request.method == 'POST':
		form = resourceForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('success/')
	else:
		print "get method"
		form = resourceForm()
	return render(request, 'requestManager/create.html', {'form':form})

def createSuccess(request):
	return render(request, 'requestManager/success.html')

def search(request):
	if request.GET:
		print "yes get"
		form = resourceSearchForm(request.GET)
		if form.is_valid():
			print "form is_valid"
			results = form.get_result_queryset()
			print results
		else:
			results = []
	else:
		form = resourceSearchForm()
		results = []

	return render_to_response('requestManager/search.html',RequestContext(request, {'form':form, 'results': results,}))