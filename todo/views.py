from django.shortcuts import render, get_object_or_404
from .models import Task

# Create your views here.

def list(request):
    tasks = Task.objects.filter(delete_flag=False, finished_date__isnull=True)
    return render(request, 'todo/list.html', {"tasks": tasks})

def finish(request, pk):
    if request.method == 'POST':
        task = get_object_or_404(Task, pk=pk)
        task.finish_task()
        tasks = Task.objects.filter(delete_flag=False, finished_date__isnull=True)
    return render(request, 'todo/list.html', {"tasks": tasks})

def submit(request):
    if request.method == 'POST':
        print('======post=====')
        task = Task()
        task.subject = request.POST['subject']
        task.note = request.POST['note']
        task.save()
        print(task)
        print('======end=====')
    tasks = Task.objects.filter(delete_flag=False, finished_date__isnull=True)
    return render(request, 'todo/list.html', {"tasks": tasks})