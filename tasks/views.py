from django.shortcuts import render, redirect
from tasks.models import Task
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.http import HttpResponse
def list_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/list.html', {'tasks': tasks})

def complete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.completed = True
    task.save()
    return redirect('list_tasks')
def change_task_status(request, pk):
    task = Task.objects.get(pk=pk)
    task.completed = not task.completed
    task.save()
    tasks = Task.objects.all()
    return render(request, 'tasks/list.html', {'tasks': tasks, 'success': True, 'message': "Task updated successfully!"})

def add_task(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            task =Task.objects.create(name=name)
            task.save()
            tasks = Task.objects.all()
            return render(request, 'tasks/task.html',{'tasks':tasks,'task':task,'success': True, 'message': "Task added successfully!"})
        else:
            return JsonResponse({'success': False, 'message': "Please enter a valid task name."})

