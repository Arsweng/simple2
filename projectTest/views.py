from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import admin

def home(request):
    return render(request, 'main/index.html')

    
