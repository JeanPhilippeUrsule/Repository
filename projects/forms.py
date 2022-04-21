from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProjectFormulary(forms.Form):
    title = forms.CharField(max_length=200)
    date_start = forms.DateField()
    date_end = forms.DateField()
    resume = forms.CharField(max_length=50)
    description = forms.CharField()
    technology = forms.CharField(max_length=50)
    #image = forms.FilePathField(path="/img")
    
class TutorFormulary(forms.Form):
    name_student = forms.CharField(max_length=200)
    title = forms.CharField(max_length=200)
    date_start = forms.DateField()
    date_end = forms.DateField()
    description = forms.CharField()
    
class PaperFormulary(forms.Form):
    title = forms.CharField(max_length=200)
    date = forms.DateField()
    description = forms.CharField()

class UserRegisterForm(UserCreationForm):
    #datos basicos del usuario
    email = forms.EmailField()
    password1 = forms.CharField(label= 'Password', widget= forms.PasswordInput)
    password2 = forms.CharField(label= 'Password confirmation', widget=forms.PasswordInput)
    last_name: forms.CharField()
    first_name: forms.CharField()

    class Meta:
        model = User                                               
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name']
        labels = {'username': 'username', 'email':'email','last_name': 'last name', 'first_name':'first name'}
        help_texts= {k:"" for k in fields}

class UserEditForm(UserCreationForm): 
    
    email = forms.EmailField(label='modifie email')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        help_texts= {k:"" for k in fields}  

