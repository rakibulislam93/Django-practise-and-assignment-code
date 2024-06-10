from django.shortcuts import render,redirect
from musician.forms import musicianForm
from musician.models import musicianModel
# Create your views here.

# def add_musician(request):
#     musician_form = musicianForm(request.POST)
#     return render(request,'musician.html',{'form':musician_form})

def add_musician(request):
    if request.method == 'POST':
        album_form = musicianForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('add_musician')
    else:
        album_form = musicianForm()
    return render(request,'album.html',{'form':album_form})


def edit_musician(request,id):
    musicians = musicianModel.objects.get(pk=id)
    musician_form = musicianForm(instance=musicians)
    
    if request.method == 'POST':
        musician_form = musicianForm(request.POST,instance=musicians)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('homepage')
    
    return render(request,'musician.html',{'form':musician_form})


