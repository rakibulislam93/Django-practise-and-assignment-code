from django.urls import path
from . import views
urlpatterns = [
    path('task/',views.task_show,name='task_show'),
]
