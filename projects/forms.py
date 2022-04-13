from django import forms

class ProjectFormulary(forms.Form):
    title = forms.CharField(max_length=200)
    date_start = forms.DateField()
    date_end = forms.DateField()
    resume = forms.CharField(max_length=50)
    description = forms.CharField()
    technology = forms.CharField(max_length=50)
    
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
    

