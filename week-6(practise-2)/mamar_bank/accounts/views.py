from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import FormView
from . forms import UserRegisterForm,UserUpdateForm
from django.contrib.auth import login,logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView
from django.views import View
from transactions.views import transaction_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
# Create your views here.


class UserRegisterView(FormView):
    template_name = 'accounts/user_registration.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('register')

    def form_valid(self, form):
        user = form.save()
        login(self.request,user)
        return super().form_valid(form) # form_valid function call hobe jodi sob thik thake
    


class UserLoginView(LoginView):
    template_name = 'accounts/user_login.html'
    
    def get_success_url(self) -> str:
        return reverse_lazy('homepage')
    

class UserLogoutView(LogoutView):
    
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('homepage')
    

class UserBankAccountUpdateView(View):
    template_name = 'accounts/profile.html'

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the user's profile page
        return render(request, self.template_name, {'form': form})
    


class UserPassChange(PasswordChangeView):
    template_name = 'accounts/pass_change.html'
    success_url = reverse_lazy('profile')
    
    def form_valid(self, form):
        form = super().form_valid(form)
        
        subject = "Password Change"
        to_mail = self.request.user.email
        message = render_to_string('accounts/pass_change_mail.html',{
            'user': self.request.user
        })
        sent_mail = EmailMultiAlternatives(subject,to=[to_mail])
        sent_mail.attach_alternative(message,'text/html')
        sent_mail.send()
        return form
         
    
    
    