from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from album.forms import albumForm
from album.models import albumModel

from django.views.generic import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
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


# using class based view

class AddAlbumCreateView(LoginRequiredMixin,CreateView):
    model = albumModel
    form_class = albumForm
    template_name = 'album.html'
    success_url = reverse_lazy('add_album')
    login_url = 'loginpage'

    def form_valid(self, form):
        return super().form_valid(form)

@login_required
def edit_album(request,id):
    album = albumModel.objects.get(pk=id)
    album_form = albumForm(instance=album)

    if request.method=='POST':
        album_form = albumForm(request.POST,instance=album)
        if album_form.is_valid():
            album_form.save()
            return redirect('homepage')
    
    return render(request,'album.html',{'form':album_form})


# edit album using class based view

class EditAlbumView(LoginRequiredMixin,UpdateView):
    model = albumModel
    form_class = albumForm
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')
    template_name = 'album.html'
    login_url = 'loginpage'
    


def delete_album(request,id):
    albums = albumModel.objects.get(pk=id)
    albums.delete()
    return redirect('homepage')


# delite using class based view..

class AlbumDeleteView(LoginRequiredMixin,DeleteView):
    model = albumModel
    pk_url_kwarg = 'id'
    template_name = 'delete.html'
    success_url = reverse_lazy('homepage')
    login_url = 'loginpage'