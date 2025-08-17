from django.shortcuts import render

from .models import Task



def index2(request):
    tasks = Task.objects.all()
    return render(request, 'notes/index.html', {'title': 'Main page of the task page', 'tasks': tasks})

