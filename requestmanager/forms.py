from django.forms import ModelForm
from requestmanager.models import requested


class MyRequestForm(ModelForm):
    
    class Meta:
        model = requested
        fields = ('name', 'publisher', 'edition', 'subscription_type', 'comment')
        # labels = {
        #     'name': ('Book/Journal'),
        #     'publisher': ('published by'),
        #     'edition': ('edition'),
        #     'subscription_type':('1-Book 2- Journal')
        # }
        
    # def save(self, commit=True):
    #     requested = super(MyRequestForm, self).save(commit=False)
    #     # user.set_password(self.cleaned_data['password1'])
        
    #     if commit:
    #         requested.save()
            

    
    # name = models.CharField(max_length=50)
    # publisher = models.CharField(max_length=50)
    # edition = models.CharField(max_length=50)
    # subscription_type = models.BooleanField(default=True)
    # comment = models.CharField(max_length=200)
    
    
