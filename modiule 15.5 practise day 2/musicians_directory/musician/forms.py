from django import forms
from . import models
class musicianForm(forms.ModelForm):
    
    class Meta:
        model = models.musicianModel
        fields = '__all__'
