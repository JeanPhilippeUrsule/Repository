from django.urls import path
from projects import views

urlpatterns = [
    path('', views.index, name='Index'),
    path('project', views.project_index, name='project_index'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('tutor/', views.tutor_index, name='tutor_index'),
    path('tutor/<int:pk>/', views.tutor_detail, name='tutor_detail'),
    path('paper/', views.paper_index, name='paper_index'),
    path('paper/<int:pk>/', views.paper_detail, name='paper_detail'),
    path('projectFormulary', views.projectFormulary, name='ProjectFormulary'),
    path('tutorFormulary', views.tutorFormulary, name='TutorFormulary'),
    path('paperFormulary', views.paperFormulary, name='PaperFormulary'),
    path('projectSearch/', views.projectSearch, name='projectSearch'),
    path('searchProject/', views.searchProject),
    
]