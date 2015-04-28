from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from requestManager.models import resource

# Create your views here.
def reqManager(request):
    latest_request = resource.objects.order_by('-creation_date')[:10]
    context = {'latest_request': latest_request}
    return render(request, 'requestManager/index.html', context)
    
def detail(request, resource_id):
    r = get_object_or_404(resource, pk=resource_id)
    return render(request, 'requestManager/detail.html', {'r': r})
