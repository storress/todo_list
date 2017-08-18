# -*- coding: utf-8 -*-
from django.test import TestCase
from todolist.models import *
import pdb
# Create your tests here.


class TaskTestCaseAddDeleteTask(TestCase):
    
    
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
        
class TestCaseIsDone(TestCase):
    
    def setUp(self):
        global task, task_name
        # pdb.set_trace()
        task_name = "My first task"
        task = Task(name = task_name)
        task.save()
        
        
    
    def testTaskIsDone(self):
        task = Task.objects.get()
        task.complete()
        task1 = Task.objects.get()
        self.assertTrue(task1.isDone)

class TestEditTask(TestCase):
    
    def setUp(self):
        global task, task_name
        # pdb.set_trace()
        task_name = "My first task"
        task = Task(name = task_name)
        task.save()
        
    def testEditTask(self):
        #arrange
        task_name2 = "My edited task"
        
        #act
        status = task.edit(name = task_name2)
        
        #assert
        self.assertEquals(task.name, task_name2)
        self.assertEquals(status, True)
        
        
    def testPreventNotCompletedDuplicate(self):
        #arrange
        #tarea no completada en lista
        task2_name = "My second task"
        task2 = Task(name = task2_name)
        task2.save()
        
        #act
        #usar nombre de tarea no completada
        status_edit_fail = task.edit(task2_name)
        
        
        #assert
        self.assertNotEqual(task.name, task2_name)
        self.assertEqual(task.name, task_name)
        self.assertEquals(status_edit_fail, False)
        
        
    def testAllowCompletedTaskDuplicate(self):
        #arrange
        #tarea completada
        task3_name = "Completed task"
        task3 = Task(name = task3_name, done = True)
        task3.save()
        
        #act
        #usar nombre de tarea completada
        status_edit_done = task.edit(task3_name)
        
        #assert
        self.assertEquals(task.name, task3_name)
        self.assertEquals(status_edit_done, True)