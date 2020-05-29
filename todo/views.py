from django.shortcuts import render
from .models import Task

# Create your views here.

def list(request):
    tasks = Task.objects.filter(delete_flag=False, finished_date__isnull=True)
    return render(request, 'todo/list.html', {"tasks": tasks})