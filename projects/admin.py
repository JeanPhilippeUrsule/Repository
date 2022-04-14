from django.contrib import admin
from .models import *
# Register your models here.

#Necesito los permisos de administrador para las " class " que tengo

admin.site.register(Project)
admin.site.register(Paper)
admin.site.register(Tutor)