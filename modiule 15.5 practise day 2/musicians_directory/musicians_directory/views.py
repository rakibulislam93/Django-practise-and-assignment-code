from django.shortcuts import render
from album.models import albumModel
def home(request):
    all_data = albumModel.objects.all()
    return render(request,'home.html',{'data':all_data})