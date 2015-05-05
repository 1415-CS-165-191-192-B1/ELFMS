from django.db.models import Q
from simple_search import BaseSearchForm
from django import forms
from django.forms import ModelForm
from requestManager.models import resource


class resourceForm(ModelForm):
    comment = forms.CharField(required=False)
    class Meta:
        model = resource
        fields = '__all__'

class resourceSearchForm(BaseSearchForm):
	class Meta:
		base_qs = resource.objects
		search_fields = ('title','^author', '=id')
		#fulltext_indexes = (('title', 2), ('title, author, id', 1),)