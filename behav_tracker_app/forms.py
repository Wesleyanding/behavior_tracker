from django import forms
from .models import Behavior, Student 

class NewBehavForm(forms.Form):
    antecedent = forms.CharField(max_length=50)
    behavior = forms.CharField(max_length=50)
    intervention = forms.CharField(max_length=50)
    location = forms.CharField(max_length=50)
