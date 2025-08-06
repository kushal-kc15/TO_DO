from django.shortcuts import render
from django.http import HttpResponse
from todo_app.models import task

def home(request):
    tasks = task.objects.filter(completed=False).order_by('-updated_at')
    context = {
        'tasks': tasks
    }
    return render(request, 'home.html', context)
