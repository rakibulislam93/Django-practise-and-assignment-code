from django.shortcuts import render,redirect
from . forms import RegisterForm,UpdateForm
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def home(request):
    return render(request,'home.html') 


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request,'Account created succefully done')
            form.save()
            return redirect('registerpage')
    
    else:
        form = RegisterForm()
    return render(request,'register.html',{'form':form})
    


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            print(user_name)
            print(user_pass)
            user = authenticate(request,username= user_name , password = user_pass)

            if user is not None:
                messages.success(request,f'You are logged in as {user_name}')
                login(request,user)
                return redirect('profilepage')
            
            
        else:
            messages.warning(request,'Invalid username or password')
            return redirect('loginpage')
    else:
        form = AuthenticationForm()
        return render(request,'login.html',{'form':form})
    
def user_logout(request):
    logout(request)
    messages.success(request,'Logout successfull')
    return redirect('homepage')


def profile(request):
    return render(request,'profile.html')

def editProfile(request):
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'Profile update successfully..')
            return redirect('profilepage')
    else:
        form = UpdateForm(instance=request.user)
    return render(request,'update_profile.html',{'form':form})


def normalpasschange(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            messages.success(request,'Your password change successfully..')
            return redirect('profilepage')
    else:
        form = PasswordChangeForm(request.user)
    return render(request,'pass_change.html',{'form':form})


def PassChangeWithoutOldPass(request):
    if request.method == 'POST':
        form = SetPasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password has been changed successfully.')
            return redirect('profilepage')
    else:
        form = SetPasswordForm(request.user)
        
    return render(request, 'pass_change.html', {'form': form})