from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='homepage'),
    path('brand/<slug:brand_slug>/',views.home,name='brand_wise_car'),
    path('register/',views.UserRegister,name='registerpage'),
    path('login/',views.UserLogin.as_view(),name='loginpage'),
    path('logout/',views.UserLogout,name='logoutpage'),
    path('profile/',views.profile,name='profilepage'),
    path('details/<int:id>',views.DetailCarView.as_view(),name='detail_car'),
    path('buy/<int:id>',views.buyCar,name='buy_car'),
    path('pass_change',views.Password_change_view.as_view(),name='pass_change'),
    path('update_profile/',views.UpdateProfile,name='update_profile'),
    
]
