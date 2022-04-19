from django.db import models

# Create your models here.

#Category para ordenar los posts
class Category(models.Model):
    name = models.CharField(max_length=20)

#Los Posts con fecha de modificacion y asociacion a una o mas categorias
class Post(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')

#Los comentarios que son asociados unicamente al post en el cual esta
class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)