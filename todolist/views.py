from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from todolist.models import *

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
    task_name = request.POST.get('task')
    duplicated = Task.verifyDuplicate(task_name)
    #pdb.set_trace()
    try:
        if(not duplicated):
            Task(name = task_name).save()
        todo_list = Task.objects.filter(done = False)
        completed_tasks = Task.objects.filter(done = True)
        # Se agregaron las variables add_status y task_name, que corresponden al estado de si se agrego o no (lo cual depende de si la 
        # tarea esta duplicada o no) ademas del nombre de la tarea, en caso de que este duplicada, para darle la informacion al usuario.
    except ValidationError:
        pass
    context = { "todo_list": todo_list, "completed_tasks": completed_tasks, "add_status" : not duplicated, "task_name" : task_name}
    return render(request, "todolist/index.html", context)
    
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
    if(not status):
        todo_list = Task.objects.filter(done = False)
        completed_tasks = Task.objects.filter(done = True)
        context = { "todo_list": todo_list, "completed_tasks": completed_tasks, "edit_status" : status, "task_name" : new_name}
        return render(request, "todolist/index.html", context)
    return redirect("index")