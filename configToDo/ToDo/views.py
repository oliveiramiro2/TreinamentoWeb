from django.db import models
from django.shortcuts import render, get_object_or_404
from .models import Task

def homePage(request):
    tasks = Task.objects.all()
    return render(request, 'todo/index.html', {'tasks': tasks})

def taskView(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'todo/task.html', {'task': task})
