from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.UserRegisterView.as_view(),name='register'),
    path('login/',views.UserLoginView.as_view(),name='loginpage'),
    path('logout/',views.UserLogoutView.as_view(),name='logoutpage'),
    path('profile/',views.UserBankAccountUpdateView.as_view(), name='profile' ),
    path('pass_change',views.UserPassChange.as_view(),name='pass_change'),
]
