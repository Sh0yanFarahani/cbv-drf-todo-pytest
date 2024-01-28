from django.db import models

# Create your models here.

class Task(models.Model):
    ''' a model for todo app '''

    name = models.CharField(max_length=125)
    done = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name