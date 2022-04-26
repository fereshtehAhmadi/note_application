from django.db import models


class notes(models.Model):
    title = models.CharField(max_length=100)
    note = models.CharField(max_length=40000)
    date = models.DateTimeField(auto_now_add=True)
    
