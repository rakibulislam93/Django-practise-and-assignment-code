from django.shortcuts import render,redirect
from album.forms import albumForm
from album.models import albumModel
# Create your views here.

def add_album(request):
    if request.method == 'POST':
        album_form = albumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('add_album')
    else:
        album_form = albumForm()
    return render(request,'album.html',{'form':album_form})



def edit_album(request,id):
    album = albumModel.objects.get(pk=id)
    album_form = albumForm(instance=album)

    if request.method=='POST':
        album_form = albumForm(request.POST,instance=album)
        if album_form.is_valid():
            album_form.save()
            return redirect('homepage')
    
    return render(request,'album.html',{'form':album_form})


def delete_album(request,id):
    albums = albumModel.objects.get(pk=id)
    albums.delete()
    return redirect('homepage')


