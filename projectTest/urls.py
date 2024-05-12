from django.contrib import admin
from django.urls import path,include
from .views import home
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name = 'home'),
    path('books/',include('books.urls')),
    path('users/',include('users.urls')),
]

urlpatterns += static( settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )
