from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from todo_app.models import task

# Create your views here.
def addTask(request):
    Task=request.POST.get('task')
    task.objects.create(task=Task)
    return redirect('home')

def completeTask(request,pk):
    Task= get_object_or_404(task, pk=pk)
    Task.completed = True
    Task.save()
    return redirect('home')

def deleteTask(request, task_id):
    Task = get_object_or_404(task, id=task_id)
    Task.delete()
    return redirect('home')

def undoneTask(request, pk):
    Task=get_object_or_404(task, pk=pk)
    Task.completed=False
    Task.save()
    return redirect('home')

def updateTask(request, pk):
    Task = get_object_or_404(task, pk=pk)
    if request.method == 'POST':
        Task.task = request.POST.get('task')
        Task.save()
        return redirect('home')
    return render(request, 'update_task.html', {'task': Task})