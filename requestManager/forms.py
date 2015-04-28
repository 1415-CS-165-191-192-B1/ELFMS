from django.forms import ModelForm
from requestManager.models import resource


class resourceForm(ModelForm):
    class Meta:
        model = resource
        fields = '__all__'