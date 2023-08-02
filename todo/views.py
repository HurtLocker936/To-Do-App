from django.shortcuts import render, redirect
from django.http import HttpResponse
from todo.models import Task
# Create your views here.
from .serializers import TaskSerializer


def AddTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')


def MarkTask(request, pk):
    task_obj = Task.objects.get(id=pk)
    task_obj.is_completed = True
    task_obj.save()
    return redirect('home')


def DeleteTask(request, pk):
    task_obj = Task.objects.get(id=pk)
    task_obj.delete()
    return redirect('home')


def MarkUndone(request, pk):
    task_obj = Task.objects.get(id=pk)
    task_obj.is_completed = False
    task_obj.save()
    return redirect('home')

def EditTask(request, pk):
    task = request.POST['task']
    task_obj = Task.objects.get(id=pk)
    task_obj.task = task
    task_obj.save()
    return redirect('home')
