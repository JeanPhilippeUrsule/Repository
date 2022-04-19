from dataclasses import fields
from projects.models import Project, Paper, Tutor, Avatar
from django.http import HttpResponse
from django.shortcuts import render
from projects.forms import ProjectFormulary, TutorFormulary, PaperFormulary

#Ahora vamos a simplificar lo que teniamos usando funciones de Django
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

#Aca agregamos lo del Login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate

#Vamos a tener 2 tipos de vistas, una general y una detallada, mas los diferentesformularios y buscador

#Vistas generales______________________________ 

def index(request):
    
    #avatares = Avatar.objects.filter(user=request.user.id)
    
    #return render(request,'projects/index.html', {'url':avatares[0].imagen.url})
    return render(request,'projects/index.html')
def project_index(request):
    projects = Project.objects.all()#levantamos todos los objetos de la class Project
    context = {
        'projects': projects
    }#creamos el diccionario
    return render(request, 'projects/project_index.html', context) #linkeamos el diccionario con un html

def paper_index(request):
    papers = Paper.objects.all()
    context = {
        'papers': papers
    }
        
    return render(request,'projects/paper_index.html', context)

def tutor_index(request):
    tutors = Tutor.objects.all()
    context = {
        'tutors': tutors
    }
    
    return render(request,'projects/tutor_index.html',context)

#Vistas detalladas________________________________ 

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)#el pk nos permite usar el numero del projecto va ser util en un loop
    context = {
        'project': project
    }
    return render(request, 'projects/project_detail.html', context)

def paper_detail(request,pk):
    paper = Paper.objects.get(pk=pk)
    context = {
        'paper': paper
    }
        
    return render(request,'projects/paper_detail.html', context)

def tutor_detail(request,pk):
    tutor = Tutor.objects.get(pk=pk)
    context = {
        'tutor': tutor
    }
        
    return render(request,'projects/tutor_detail.html', context)

#Formularios________________________________________

def projectFormulary(request):
    
    if request.method == 'POST': #Vamos el metodo POST
        
        myFormulary = ProjectFormulary(request.POST)#aca llega toda la info
        
        if myFormulary.is_valid(): #comprobamos que cumplimos los requisitos de Django
            
            information = myFormulary.cleaned_data #vamos a acceder a este informacion como diccionario
            
            project = Project(title = information['title'], 
                              date_start = information['date_start'],
                              date_end = information['date_end'],
                              resume = information['resume'],
                              description = information['description'],
                              technology = information['technology'],
                              #image = information['image']
                              )#datos del proyecto
            project.save()#guardamos todo
            return render(request,'projects/project_index.html')
    else:
        myFormulary= ProjectFormulary()
        
    return render(request, 'projects/projectFormulary.html',{'myFormulary':myFormulary})

def tutorFormulary(request):
    
    if request.method == 'POST':
        
        myFormulary = TutorFormulary(request.POST)
        
        if myFormulary.is_valid():
            
            information = myFormulary.cleaned_data #vamos a cceder a este informacion como diccionario

            tutor = Tutor(name_student = information['name_student'],
                          title = information['title'], 
                          date_start = information['date_start'],
                          date_end = information['date_end'],
                          description = information['description']
                          )
            tutor.save()
            
            return render(request,'projects/tutor_index.html')
    else:
        myFormulary= TutorFormulary()
        
    return render(request, 'projects/tutorFormulary.html',{'myFormulary':myFormulary})

def paperFormulary(request):
    
    if request.method == 'POST':
        
        myFormulary = PaperFormulary(request.POST)
        
        if myFormulary.is_valid():
            
            information = myFormulary.cleaned_data #vamos a cceder a este informacion como diccionario

            paper = Paper(title = information['title'], 
                          date = information['date'],
                          description = information['description'],
                          )
            
            paper.save()
            return render(request,'projects/paper_index.html')
    else:
        myFormulary= PaperFormulary()
        
    return render(request, 'projects/paperFormulary.html',{'myFormulary':myFormulary})

#Buscador____________________________________________

def searchProject(request):
    
    if request.GET['title']: #buscamos con elm metodo GET el titulo
        title= request.GET['title']#Variable titulo
        project= Project.objects.filter(title__icontains=title)#variable del buscador
        
        return render(request, 'projects/searchResult.html', {'project':project, 'title':title})
    
    else:
        answer='No data send'
    
    return render(request, 'projects/searchResult.html', {'answer':answer})

def projectSearch(request):
    return render(request, 'projects/searchProject.html')

#Delete______________________________________________

def deleteProject(request, project_title):
    #Recibe el titulo del projecto que vamos a eleminar
    project = Project.objects.get(title=project_title)
    project.delete()
    
    #volvemos al menu
    projects = Project.objects.all()#levantamos todos los objetos de la class Project
    context = {
        'projects': projects
    }#creamos el diccionario
    return render(request, 'projects/project_index.html', context) #linkeamos el diccionario con un html

#Edit__________________________________________________

def editProject(request, project_title):
    
      #Recibe el titulo del projecto que vamos a modificar
       project = Project.objects.get(title=project_title)
       
       if request.method == 'POST': #Vamos el metodo POST
        
        myFormulary = ProjectFormulary(request.POST)#aca llega toda la info
        
        if myFormulary.is_valid(): #comprobamos que cumplimos los requisitos de Django
            
            information = myFormulary.cleaned_data #vamos a acceder a este informacion como diccionario
            
            project.title = information['title'] 
            project.date_start = information['date_start']
            project.date_end = information['date_end']
            project.resume = information['resume']
            project.description = information['description']
            project.technology = information['technology']
            #project.image = information['image']
                              
            project.save()
            
            return render(request,'projects/project_index.html')
       else:
            #Creo el formulario con los datos que voy a modificar
            myFormulary= ProjectFormulary(initial={'title':project.title,
                                                   'date_start':project.date_start,
                                                   'date_end':project.date_end,
                                                   'resume': project.resume,
                                                   'description': project.description,
                                                   'technology': project.technology
                                                   })
        
       return render(request, 'projects/projectFormulary.html',{'myFormulary':myFormulary, 'project_title': project_title})
    
#Listas genericas para Paper

class PaperList(ListView):
    model = Paper
    template_name = 'projects/paper_list.html'

class PaperDetail(DetailView):
    model = Paper
    template_name = 'projects/paper_detail.html'
    
class PaperCreate(CreateView):
    model = Paper
    success_url = 'projects/paper/list'
    fields = ['title', 'date', 'description']
    
class PaperUpdate(UpdateView):
    model = Paper
    success_url = 'projects/paper/list'
    fields = ['title', 'date', 'description']
    
class PaperDelete(DeleteView):
    model = Paper
    success_url = 'projects/paper/list'
    
#Listas genericas para Projects    
class ProjectList(ListView):
    model = Project
    template_name = 'projects/project_list.html' 
    
#Login,Logout,Register
def login_request(request):
    #capturamos el post
    if request.method == 'POST':
        #inicio el uso del formulario de autenticación que me da Django
        #me toma dos parámetros el request y los datos que toma del request
        form = AuthenticationForm(request, data = request.POST)
            
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username = usuario, password = contra)
            #print(1)
            if user is not None:
                login(request, user)#toma 2 atributos, request y user
                
                return render(request, 'projects/index.html', {'mensaje': f'Welcome {usuario}'})
            else:
                #print(2)
                return render(request, 'projects/index.html', {'mensaje':'Error in the data'})
        else:
                return render(request, 'projects/index.html', {'mensaje':'Error in the formulary'})
        
        #al final recuperamos el form
    form = AuthenticationForm()
    #print(3)
    return render(request, 'projects/login.html', {'form': form})
  
def register(request):
      
      if request.method == "POST":

            form = UserCreationForm(request.POST)

            if form.is_valid():
                  username = form.cleaned_data['username']
                  form.save()

                  return render(request, 'projects/index.html', {'message': 'user created'})

      else: 
            form = UserRegisterForm()

      return render(request, 'projects/register.html', {'form': form} )
  
