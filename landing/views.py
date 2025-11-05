from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.contrib import messages


def home(request):
    tasks = Task.objects.filter(is_archived=False)
    return render(request, 'design/home.html', {'tasks': tasks})

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
    was_archived = task.is_archived
    task.delete()
    # Redirect based on where the request came from
    next_url = request.POST.get('next') or request.GET.get('next')
    if next_url:
        return redirect(next_url)
    # Fallback: redirect based on task state before deletion
    return redirect('archived_tasks' if was_archived else 'home')

def edit_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == 'POST':
        new_name = request.POST.get('name')
        if new_name:
            task.name = new_name
        task.save()
        # Redirect based on where the request came from
        next_url = request.POST.get('next') or request.GET.get('next')
        if next_url:
            return redirect(next_url)
        # Fallback: redirect based on task state
        return redirect('archived_tasks' if task.is_archived else 'home')
    return render(request, 'design/edit.html', {'task': task})

def archive_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.is_archived = not task.is_archived
    task.save()
    return redirect('archived_tasks' if task.is_archived else 'home')

def toggle_archive(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_archived = not task.is_archived  # Toggle True/False
    task.save()
    # Redirect based on where the request came from
    next_url = request.POST.get('next') or request.GET.get('next')
    if next_url:
        return redirect(next_url)
    # Fallback: redirect based on new state
    return redirect('archived_tasks' if task.is_archived else 'home')

def archived_tasks(request):
    tasks = Task.objects.filter(is_archived=True)
    return render(request, 'design/archive.html', {'tasks': tasks})