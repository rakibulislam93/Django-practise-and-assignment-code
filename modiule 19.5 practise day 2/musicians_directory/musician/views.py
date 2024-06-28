from typing import Any
from django.contrib.auth.forms import AuthenticationForm
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from musician.forms import musicianForm
from musician.models import musicianModel

from . forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

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


# using calss bese view
class AddMusicianView(LoginRequiredMixin,CreateView):
    model = musicianModel
    form_class = musicianForm
    template_name = 'album.html'
    success_url = reverse_lazy('add_musician')
    login_url = 'loginpage'

    def form_valid(self, form):
        return super().form_valid(form)

def edit_musician(request,id):
    musicians = musicianModel.objects.get(pk=id)
    musician_form = musicianForm(instance=musicians)
    
    if request.method == 'POST':
        musician_form = musicianForm(request.POST,instance=musicians)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('homepage')
    
    return render(request,'musician.html',{'form':musician_form})

# edit musician class based view...
class EditMusicianView(LoginRequiredMixin,UpdateView):
    model = musicianModel
    form_class = musicianForm
    template_name = 'musician.html'
    success_url = reverse_lazy('homepage')
    pk_url_kwarg = 'id'
    login_url = 'loginpage'
    

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account crate successfull')
            return redirect('registerpage')
    else:
        form = RegisterForm()
    return render(request,'register.html',{'form':form})


class UserLoginView(LoginView):
    
    template_name = 'login.html'
    
    def get_success_url(self) -> str:
        return reverse_lazy('profilepage')
    
    def form_valid(self, form: AuthenticationForm):
        messages.success(self.request,'Logged in successful')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid your information')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

@login_required
def profile(request):
    return render(request,'profile.html')





class UserLogoutView(LogoutView):
    
    next_page = reverse_lazy('loginpage')  # Redirect to login page after logout

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            #  logout only for authenticated users
            
            return super().dispatch(request, *args, **kwargs)
        else:
            
            return redirect(self.next_page)
