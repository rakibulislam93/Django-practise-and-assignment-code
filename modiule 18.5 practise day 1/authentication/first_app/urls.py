from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='homepage'),
    path('register/',views.register,name='registerpage'),
    path('login/',views.user_login,name='loginpage'),
    path('logout/',views.user_logout,name='logoutpage'),
    path('profile/',views.profile,name='profilepage'),
    path('edit_profile/',views.editProfile,name='edit_profile'),
    path('pass_change/',views.normalpasschange,name='pass_change'),
    path('pass_change_old/',views.PassChangeWithoutOldPass,name='pass_change_old'),
]
