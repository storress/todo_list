from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.


# se define el modelo para una Task
# basta con esto para que se genere un listado con tasks
class Task(models.Model):
    name = models.CharField(max_length = 100, null = False)
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
            try:
                self.save()
                return True
            except ValidationError:
                return False
        return False
    
    def save(self, *args, **kwargs):
        """ Checks whether a task is duplicated or empty of just spaces and avoids saving that 
        task """
        try:
            self.full_clean()
        except ValidationError:
            return
        duplicated = Task.verifyDuplicate(self.name)
        if self.name != '' and not self.name.isspace() and not duplicated:
            return super(Task,self).save(*args, **kwargs)
        return
        

        
    @staticmethod
    def verifyDuplicate(task_name):
        tasks = Task.objects.filter(name = task_name, done = False)
        if tasks:
            return True
        return False
        