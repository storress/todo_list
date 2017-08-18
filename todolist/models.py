from __future__ import unicode_literals

from django.db import models

# Create your models here.


# se define el modelo para una Task
# basta con esto para que se genere un listado con tasks
class Task(models.Model):
    name = models.CharField(max_length = 100, blank = False, null = False)
    done = models.BooleanField(default = False)
    
    def complete(self):
        self.done = True
        self.save()
    
    def isDone(self):
        return self.done
    
    def edit(self, name=None):
        if name is None:
            return False
        
        if not Task.verifyDuplicate(name):
            self.name = name
            self.save()
            return True
            
        return False
        
    @staticmethod
    def verifyDuplicate(task_name):
        tasks = Task.objects.filter(name = task_name, done = False)
        if tasks:
            return True
        return False
        