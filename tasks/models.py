#MOdels are used to create tables in DB

from django.db import models
# A table of name Task is created having 3 fields 'title', 'complete','created'
class Task(models.Model):
    title=models.CharField(max_length=200)
    complete=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)

#object will be identified by this in DB
    def __str__(self):
        return self.title

# class Student(models.Model):
#     name = models.CharField(max_length=200)
#     roll = models.CharField(max_length=200)
    
