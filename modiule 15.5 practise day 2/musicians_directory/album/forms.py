from django import forms
from . import models
class albumForm(forms.ModelForm):
    
    class Meta:
        model = models.albumModel
        fields = '__all__'
        
