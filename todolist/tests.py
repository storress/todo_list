# -*- coding: utf-8 -*-
from django.test import TestCase
from models import *
import pdb
# Create your tests here.


class TaskTestCase(TestCase):
    
    
    def setUp(self):
        global task, task_name
        # pdb.set_trace()
        task_name = "My first task"
        task = Task(name = task_name)


    #se crea una Task y se agrega al listado de Tasks
    #para validar que se guardó correctamente,
    #se comprueba que el nombre de la tarea guardada coincida y además
    #se verifica que el largo del listado de tareas haya crecido en uno
    def testAddTask(self):
        #arrange
        list_len = len(Task.objects.all())
        
        #act
        task.save()
        list_len2 = len(Task.objects.all())
        task1 = Task.objects.get()
        
        #assert
        self.assertEquals(list_len + 1, list_len2)
        self.assertEquals(task.name, task_name)
        self.assertEquals(task1.name, task_name)
        
    def testDeleteTask(self):
        
        #arrange
        tasks_len1 = len(Task.objects.all())
        task.save()
        tasks_len2 = len(Task.objects.all())
        
        #act
        task.delete()
        tasks_len3 = len(Task.objects.all())
        
        #assert
        self.assertEquals(tasks_len1 + 1, tasks_len2)
        self.assertEquals(tasks_len1, tasks_len3)
        
        
        
        
        
        
        
            
        
    