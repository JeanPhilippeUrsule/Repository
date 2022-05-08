from django.urls import path
from projects import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.index, name='Index'),
    path('project', views.project_index, name='project_index'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('tutor/', views.tutor_index, name='tutor_index'),
    path('tutor/<int:pk>/', views.tutor_detail, name='tutor_detail'),
    path('paper/', views.paper_index, name='paper_index'),
    path('paper/<int:pk>/', views.paper_detail, name='paper_detail'),
    path('about/', views.about, name='about'),
    
    path('projectFormulary', views.projectFormulary, name='ProjectFormulary'),
    path('tutorFormulary', views.tutorFormulary, name='TutorFormulary'),
    path('paperFormulary', views.paperFormulary, name='PaperFormulary'),
    path('projectSearch/', views.projectSearch, name='projectSearch'),
    path('searchProject/', views.searchProject),
   
    path('deleteProject/<project_title>/', views.deleteProject, name='DeleteProject'),
    path('editProject/<project_title>/', views.editProject, name='EditProject'),
    path('deletePaper/<paper_title>/', views.deletePaper, name='DeletePaper'),
    path('editPaper/<paper_title>/', views.editPaper, name='EditPaper'),
    path('deleteTutor/<tutor_student>/', views.deleteTutor, name='DeleteTutor'),
    path('editTutor/<tutor_student>/', views.editTutor, name='EditTutor'),
    
    path('paper/list', views.PaperList.as_view(), name='PaperList'),
    path(r'^(?P<pk>\d+)$', views.PaperDetail.as_view(), name='Detail'),
    path(r'^new$', views.PaperCreate.as_view(), name='New'),
    path(r'^edit/(?P<pk>\d+)$', views.PaperUpdate.as_view(), name='Edit'),
    path(r'^delete/(?P<pk>\d+)$', views.PaperDelete.as_view(), name='Delete'),
    
    path('login', views.login_request, name='Login'),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='projects/logout.html'), name='Logout'),
    path('editProfile', views.editProfile, name='EditProfile'),
    
]