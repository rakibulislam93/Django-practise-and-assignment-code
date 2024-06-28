from django.urls import path
from . import views
urlpatterns = [
    # path('add/',views.add_album,name='add_album'),
    path('add/',views.AddAlbumCreateView.as_view(),name='add_album'),
    # path('edit/<int:id>',views.edit_album,name='edit_album'),
    path('edit/<int:id>',views.EditAlbumView.as_view(),name='edit_album'),
    path('delete/<int:id>',views.AlbumDeleteView.as_view(),name='delete_album'),
]
