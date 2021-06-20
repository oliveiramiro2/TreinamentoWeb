from django.contrib import messages
from django.core.paginator import Paginator
from ToDo.forms import TaskForm
from django.db import models
from django.shortcuts import redirect, render, get_object_or_404, redirect
from .models import Task

def homePage(request):
    tasks_list = Task.objects.all().order_by('-created_at')
    paginator = Paginator(tasks_list, 5)
    page = request.GET.get('page')
    tasks = paginator.get_page(page)
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
    
def editTask(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task.save()
            return redirect('/')
        else:
            return render(request, 'todo/edittask.html', {'form': form, 'task': task})
        
    else:
        return render(request, 'todo/edittask.html', {'form': form, 'task': task})
    
def delTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()
    messages.info(request, 'Tarefa deletada com sucesso!!')
    return redirect('/')
