from django.shortcuts import render, redirect
from django.http import HttpResponse
from models import *

import pdb

# Create your views here.


#vista principal, que carga el listado de tareas (tasks)
def index(request):
    todo_list = Task.objects.filter(done = False)
    completed_tasks = Task.objects.filter(done = True)
    context = { "todo_list": todo_list, "completed_tasks": completed_tasks}
    return render(request, "todolist/index.html", context)


#vista que recibe la task a agregar y la guarda en la base de datos
#redirecciona hacia index ya que no tiene un template definido
def addTask(request):
    Task(name = request.POST.get('task')).save()
    return redirect('index')
    
    
def deleteTask(request, task_id):
    Task.objects.all().filter(id = task_id).delete()
    return redirect("index")
    
def completeTask(request, task_id):
    Task.objects.all().filter(id = task_id).update(done = True)
    return redirect("index")
    
def editTask(request):
    new_name = request.POST.get('new_name')
    task_id = request.POST.get('task_id')
    # pdb.set_trace()
    status = Task.objects.all().filter(id = task_id)[0].edit(new_name)  # Si explota, es aqui
    return redirect("index")