from ToDo.forms import TaskForm
from django.db import models
from django.shortcuts import redirect, render, get_object_or_404, redirect
from .models import Task

def homePage(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'todo/index.html', {'tasks': tasks})

def taskView(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'todo/task.html', {'task': task})

def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.done = '1'
            task.save()
            return redirect('/')
    else:
        form = TaskForm()
        return render(request, 'todo/addtask.html', {'form': form})
