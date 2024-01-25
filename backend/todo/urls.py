from django.contrib import admin
from django.urls import path
from . import views

app_name = 'task'

urlpatterns = [
    path('', views.TaskList.as_view(), name='task-list'),
    path('task/add', views.TaskCreate.as_view(), name='create-task'),
    path('update/<int:pk>', views.TaskUpdate.as_view(), name='task-update'),
    path('delete/<int:pk>', views.TaskDelete.as_view(), name='delete-task'),
    path('complate/<int:pk>', views.TaskComplate.as_view(), name='task-complate')

]
