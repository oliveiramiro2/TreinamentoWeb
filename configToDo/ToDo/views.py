from django.db import models
from django.shortcuts import render
from .models import Task

def homePage(request):
    tasks = Task.objects.all()
    return render(request, 'todo/index.html', {'tasks': tasks})
