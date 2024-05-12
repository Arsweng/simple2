from django.forms import ModelForm 
from .models import Book
from django import forms

class Form(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','description','price','pub_date','banner']
