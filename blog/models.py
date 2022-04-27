from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Category para ordenar los posts
class Category(models.Model):
    name = models.CharField(max_length=20)
    

#Los Posts con fecha de modificacion y asociacion a una o mas categorias
class Post(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    author = models.ForeignKey(User, verbose_name="Author", on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(verbose_name="Image", upload_to="blog", null=True, blank=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    
    def __str__(self):
        return self.title

#Los comentarios que son asociados unicamente al post en el cual esta
class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)