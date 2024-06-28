from django.urls import path
from . import views
urlpatterns = [
    # path('add/',views.add_musician,name='add_musician'),
    path('add/',views.AddMusicianView.as_view(),name='add_musician'),
    # path('edit/<int:id>',views.edit_musician,name='edit_musician'),
    path('edit/<int:id>',views.EditMusicianView.as_view(),name='edit_musician'),
    path('register/',views.register,name='registerpage'),
    path('login/',views.UserLoginView.as_view(),name='loginpage'),
    path('profile/',views.profile,name='profilepage'),
    path('logout/',views.UserLogoutView.as_view(),name='logoutpage'),
    
]
