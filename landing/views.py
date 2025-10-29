from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.contrib import messages


def home(request):
    tasks = Task.objects.all()
    return render(request, 'design/home.html', {'tasks': tasks})

def todo(request):
    return render(request, 'design/todo.html')

def list(request):
    return render(request, 'design/list.html')

def add_task(request):
    if request.method == 'POST':
        task_name = request.POST.get('task_name')
        if not task_name:  # if empty or None
            messages.error(request, "Task name cannot be empty.")
            return redirect('home')
        Task.objects.create(name=task_name)
        return redirect('home')
    
def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.delete()
    return redirect('home')

def edit_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.save()
        return redirect('home')
    return render(request, 'design/edit.html', {'task': task})

def archive_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.archived = not task.archived
    task.save()
    return redirect('home')

def toggle_archive(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.archived = not task.archived  # Toggle True/False
    task.save()
    return redirect('home')  # or whatever your main todo page name is