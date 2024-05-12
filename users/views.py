from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import UserCreateForm,LoginForm

# Create your views here.
def createUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password != confirm_password:
            render(request,'users/create.html')
        else:
            user_vel=User.objects.filter(username = username).exists()
            if user_vel:
                render(request,'users/create.html')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.first_name = firstname
                user.last_name = lastname
                user.save()
                return HttpResponse('new user created')
            print(username,password)
    return render(request,'users/create.html')

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user_check = User.objects.filter(username = username).exists()
            if user_check:
                user = authenticate(request, username = username, password = password )

                if user is not None:
                    login(request,user)
                    return redirect('books:allbooks')
                else:
                    return render(request,'users/login.html',{'form':form})
            else:
                return render(request,'users/login.html',{'form':form})
        else:
            return render(request,'users/login.html',{'form':form})
    else:
        form = LoginForm()
        return render(request,'users/login.html',{'form':form})
def logout_user(request):
    logout(request)
    return redirect('users:login')