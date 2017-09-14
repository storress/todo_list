# -*- coding: utf-8 -*-
from django.test import TestCase
from todolist.models import *
from django.core.exceptions import ValidationError
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
        
class TestBlank(TestCase):
    
    def testAddEmptyTask(self):
        # arrange
        empty_task = Task(name='')
        # act
        try:
            empty_task.save()
        except Exception:
            pass
        tasks = Task.objects.all()
        # assert
        self.assertEqual(len(tasks), 0)
        
    def testAddSpacesTask(self):
        # arrange
        spaces_task = Task(name='         ')
        # act
        spaces_task.save()
        tasks = Task.objects.all()
        # assert
        self.assertEqual(len(tasks), 0)
        
class TestPreventDuplicatedPendingTask(TestCase):
    
    def testSavedDuplicatedTask(self):
        # arrange
        task_name = "Base"
        base_task = Task(name = task_name)
        duplicated_task = Task(name = task_name)
        
        tasks_len0 = len(Task.objects.all())
        
        # act
        base_task.save()
        tasks_len1 = len(Task.objects.all())
        
        duplicated_task.save()
        tasks_len2 = len(Task.objects.all())
        
        #assert
        self.assertNotEqual(tasks_len0, tasks_len1)
        self.assertNotEqual(tasks_len0, tasks_len2)
        self.assertEqual(tasks_len1, tasks_len2)
        
class TestBugAddLongTask(TestCase):
    
    def testAddLongTask(self):
        #arrange
        task_name = "Largooooooo"*1000
        

        #act
        new_task = Task(name = task_name)
        
        #assert
        
        with self.assertRaises(ValidationError):
            new_task.full_clean()
            new_task.save()
        #self.assertTrue(True)
        
        '''Este test falla dado que la base de datos Sqlite es muy flexible
        con respecto a las constraints, lo que no es el caso para PostgreSQL
        que es una base de datos real que no es flexible con los constraints'''
        
        '''Se logro pasar el test, cambiando el tipo de error'''