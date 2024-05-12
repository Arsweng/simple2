from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('',createUser, name='create'),
    path('login/',login_user, name='login'),
    path('logout/',logout_user, name='logout'),
]
