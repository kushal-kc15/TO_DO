from django.shortcuts import redirect, render
from django.http import HttpResponse
from todo_app.models import task

# Create your views here.
def addTask(request):
    Task=request.POST.get('task')
    task.objects.create(task=Task)
    return redirect('home')