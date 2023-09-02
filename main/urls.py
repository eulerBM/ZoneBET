from django.contrib import admin
from django.urls import path, include
from home.views import home
from perfil.views import perfil
from aposta.views import page_aposta

urlpatterns = [
    path( 'accounts/' , include( 'allauth.urls' )), 
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('perfil/', perfil, name='perfil'),
    path('aposta/<int:id>', page_aposta, name='aposta'),
]
