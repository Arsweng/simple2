from django.urls import path
from .views import *

app_name = 'books'

urlpatterns = [
    path('',allbooks,name = 'allbooks'),
    path('<int:id>/',onebook,name = 'onebook'),
    path('upload/', upload, name= 'upload'),
]
