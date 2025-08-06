from django.shortcuts import render
from django.http import HttpResponse
from todo_app.models import task

def home(request):
    tasks = task.objects.filter(completed=False).order_by('-updated_at')
    completed_tasks = task.objects.filter(completed=True).order_by('-updated_at')
    context = {
        'tasks': tasks,
        'completed_tasks': completed_tasks
    }
    return render(request, 'home.html', context)
