from django.shortcuts import render, redirect
from django.http import HttpResponse
from todo.models import Task
# Create your views here.
from .serializers import TaskSerializer


def AddTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')
