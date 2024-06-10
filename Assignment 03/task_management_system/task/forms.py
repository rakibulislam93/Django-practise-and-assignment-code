from django import forms
from task.models import Task

class taskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = '__all__'

        widgets = {
            'task_assign_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }