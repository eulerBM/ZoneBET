from django.contrib import admin
from django.urls import path, include
from home.views import home, perfil

urlpatterns = [
    path( 'accounts/' , include( 'allauth.urls' )), 
    path('admin/', admin.site.urls),
    path('', home),
    path('perfil/', perfil, name='perfil'),
]
