from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms
from . models import BrandModel ,CarModel,CommentModel

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
    

class BrandForm(forms.ModelForm):
    class Meta:
        model = BrandModel
        fields = '__all__'
    

class CarForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['name','email','body']
    

class passwordChangingForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = '__all__'



class UserUpdateForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']