from django.db import models


class Categorie(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category

class Notes(models.Model):
    title = models.CharField(max_length=100)
    note = models.TextField()
    creat = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Categorie',on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.title
