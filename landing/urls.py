from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('todo/', views.todo, name='todo'),
    path('list/', views.list, name='list'),
    path('add/', views.add_task, name='add_task'),
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
    path('edit/<int:pk>/', views.edit_task, name='edit_task'),
    path('archive/<int:pk>/', views.archive_task, name='archive_task'),

    path('toggle/<int:task_id>/', views.toggle_archive, name='toggle_archive'),
]