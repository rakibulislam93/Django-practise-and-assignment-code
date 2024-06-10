from django.shortcuts import render
from task.models import Task
# Create your views here.

def task_show(request):
    all_task = Task.objects.all()
    return render(request,'task_show.html',{'task':all_task})