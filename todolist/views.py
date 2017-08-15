from django.shortcuts import render, redirect
from django.http import HttpResponse
from models import *

# Create your views here.


#vista principal, que carga el listado de tareas (tasks)
def index(request):
    todo_list = Task.objects.all()
    context = { "todo_list": todo_list }
    return render(request, "todolist/index.html", context)


#vista que recibe la task a agregar y la guarda en la base de datos
#redirecciona hacia index ya que no tiene un template definido
def addTask(request):
    Task(name = request.POST.get('task')).save()
    return redirect('index')
    
    
def deleteTask(request, task_id):
    Task.objects.all().filter(id = task_id).delete()
    return redirect("index")