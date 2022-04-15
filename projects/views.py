from projects.models import Project, Paper, Tutor
from django.http import HttpResponse
from django.shortcuts import render
from projects.forms import ProjectFormulary, TutorFormulary, PaperFormulary

#Vamos a tener 2 tipos de vistas, una general y una detallada, mas los diferentesformularios y buscador

#Vistas generales______________________________ 

def index(request):
    return render(request,'index.html')

def project_index(request):
    projects = Project.objects.all()#levantamos todos los objetos de la class Project
    context = {
        'projects': projects
    }#creamos el diccionario
    return render(request, 'project_index.html', context) #linkeamos el diccionario con un html

def paper_index(request):
    papers = Paper.objects.all()
    context = {
        'papers': papers
    }
        
    return render(request,'paper_index.html', context)

def tutor_index(request):
    tutors = Tutor.objects.all()
    context = {
        'tutors': tutors
    }
    
    return render(request,'tutor_index.html',context)

#Vistas detalladas________________________________ 

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)#el pk nos permite usar el numero del projecto va ser util en un loop
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)

def paper_detail(request,pk):
    paper = Paper.objects.get(pk=pk)
    context = {
        'paper': paper
    }
        
    return render(request,'paper_detail.html', context)

def tutor_detail(request,pk):
    tutor = Tutor.objects.get(pk=pk)
    context = {
        'tutor': tutor
    }
        
    return render(request,'tutor_detail.html', context)

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
            return render(request,'project_index.html')
    else:
        myFormulary= ProjectFormulary()
        
    return render(request, 'projectFormulary.html',{'myFormulary':myFormulary})

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
            
            return render(request,'tutor_index.html')
    else:
        myFormulary= TutorFormulary()
        
    return render(request, 'tutorFormulary.html',{'myFormulary':myFormulary})

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
            return render(request,'paper_index.html')
    else:
        myFormulary= PaperFormulary()
        
    return render(request, 'paperFormulary.html',{'myFormulary':myFormulary})

#Buscador____________________________________________

def searchProject(request):
    
    if request.GET['title']: #buscamos con elm metodo GET el titulo
        title= request.GET['title']#Variable titulo
        project= Project.objects.filter(title__icontains=title)#variable del buscador
        
        return render(request, 'searchResult.html', {'project':project, 'title':title})
    
    else:
        answer='No data send'
    
    return render(request, 'searchResult.html', {'answer':answer})

def projectSearch(request):
    return render(request, 'searchProject.html')

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
    return render(request, 'project_index.html', context) #linkeamos el diccionario con un html



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
            
            return render(request,'project_index.html')
       else:
            #Creo el formulario con los datos que voy a modificar
            myFormulary= ProjectFormulary(initial={'title':project.title,
                                                   'date_start':project.date_start,
                                                   'date_end':project.date_end,
                                                   'resume': project.resume,
                                                   'description': project.description,
                                                   'technology': project.technology
                                                   })
        
       return render(request, 'projectFormulary.html',{'myFormulary':myFormulary, 'project_title': project_title})
    
