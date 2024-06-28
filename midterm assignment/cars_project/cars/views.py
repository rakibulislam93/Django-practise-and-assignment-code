from django.shortcuts import render,redirect
from . forms import RegisterForm,CommentForm,passwordChangingForm,UserUpdateForm
from django.contrib.auth.views import LoginView,PasswordChangeView
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth import logout
from . models import CarModel,BrandModel,BuyCarModel
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request,brand_slug=None):
    data = CarModel.objects.all()
    if brand_slug is not None:
        brand = BrandModel.objects.get(slug=brand_slug)
        data = CarModel.objects.filter(brand = brand)
    brand = BrandModel.objects.all()
    return render(request,'home.html',{'car':data,'brand':brand})
    
    # return render(request,'home.html')


def UserRegister(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account create successfull')
            return redirect('registerpage')

    else:
        form = RegisterForm()
    return render(request,'register.html',{'form':form})

class UserLogin(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('profilepage')

    def form_valid(self, form):
        messages.success(self.request,'Logged in successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request,'Invalid your information')
        return super().form_invalid(form)
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        return context



@login_required
def profile(request):
    user = request.user
    purchases = user.purchases.all()
    return render(request, 'profile.html', {'user': user, 'purchases': purchases})

def UserLogout(request):
    logout(request)
    messages.success(request,'Logout successfull..')
    return redirect('loginpage')


class DetailCarView(DetailView):
    model = CarModel
    pk_url_kwarg = 'id'
    template_name = 'car_details.html'
    context_object_name='car'

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=self.request.POST)
        car = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object 
        comments = car.comments.all()
        comment_form = CommentForm() 
        

        context['comments'] = comments
        context['comment_form'] = comment_form
        
        return context



@login_required
def buyCar(request, id):
    car = CarModel.objects.get(pk=id)
    if request.method == 'POST':
        quantity = 1
        if quantity <= car.quantity:
            BuyCarModel.objects.create(user=request.user, car=car, quantity=quantity)
            car.quantity -= quantity
            car.save()
            messages.success(request,'Car Purchase Successfull')
            return redirect('detail_car',id=car.id)
        else:
            messages.error(request,'Car has no available quantity')
    return render(request, 'car_details.html', {'car': car})
        


class Password_change_view(PasswordChangeView):
    form_class = passwordChangingForm
    template_name = 'pass_change.html'
    success_url = reverse_lazy('profilepage')

    # def password_success(request):
    #     return render(request,'pass_change.html')

@login_required
def UpdateProfile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profilepage')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request,'update_profile.html',{'form':form})