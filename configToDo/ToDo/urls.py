from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='task-list'),
    path('tasks/<int:id>', views.taskView, name='task-view'),
    path('newtask/', views.newTask, name='new-task'),
    path('edit/<int:id>', views.editTask, name='edit-task'),
]