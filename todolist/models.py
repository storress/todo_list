from __future__ import unicode_literals

from django.db import models

# Create your models here.


# se define el modelo para una Task
# basta con esto para que se genere un listado con tasks
class Task(models.Model):
    name = models.CharField(max_length = 100, blank = False, null = False)