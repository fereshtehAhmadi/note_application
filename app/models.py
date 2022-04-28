from django.db import models


class Notes(models.Model):
    title = models.CharField(max_length=100)
    note = models.CharField(max_length=40000)
    creat = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now_add=True)
    

def __str__(self):
    return self.name
