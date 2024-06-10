from django.shortcuts import render
from first_app.forms import firstForm
# Create your views here.

def home ( request):
    form = firstForm(request.POST)
    return render(request,'first.html',{'form':form})