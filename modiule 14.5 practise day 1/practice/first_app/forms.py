from django import forms
from . import models

class firstForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    check = forms.BooleanField()
    date = forms.DateField(widget=forms.NumberInput(attrs={'type':'date'}))
    num = forms.DecimalField()
    CHOICES = [
        
        ('one',1),
        ('two',2),
        ('three',3),
        ('four',4),
        ('five',5),

    ]
    rating = forms.ChoiceField(choices=CHOICES)
    address = forms.CharField()
    comment = forms.CharField(widget=forms.Textarea)
  



# class firstForm(forms.Form):
#     name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter you name'}))
#     email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'Enter your email'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':"Type your password"}))
#     birthday = forms.CharField(widget=forms.DateInput(attrs={'type':'date'}))
#     address = forms.CharField(widget=forms.TextInput)

#     security_code = forms.CharField(help_text="Security code 4 digit")



# class firstForm(forms.ModelForm):
    
#     class Meta:
#         model = models.firstModel
#         fields = '__all__'


#         widgets = {
#             'name':forms.TextInput(attrs={'placeholder':'Type your name'}),
#             'date':forms.DateInput(attrs={'type':'date'})
#         }

    
