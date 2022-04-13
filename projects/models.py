from django.db import models

# Create your models here.

#Creacion de una class de los projectos que hice
class Project(models.Model):
    title = models.CharField(max_length=200)
    date_start = models.DateField()
    date_end = models.DateField()
    resume = models.CharField(max_length=50)
    description = models.TextField()
    technology = models.CharField(max_length=50)
    image = models.FilePathField(path="/img")

#Creacion de una class con los datos de los tutelados que tuve
class Tutor(models.Model):
    name_student = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    date_start = models.DateField()
    date_end = models.DateField()
    description = models.TextField()

#Creacion de una class de los ppaper que publique
class Paper(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()
    #upload = models.FileField(upload_to='uploads/')