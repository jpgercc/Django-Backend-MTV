"""
URL configuration for bibliotecaapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/', include('usuario.urls', namespace='usuario')),
    path('livro/', include('livro.urls', namespace='livro')),
    path('autor/', include('autor.urls', namespace='autor')),
    path('editora/', include('editora.urls', namespace='editora')),
    path('biblioteca/', include('biblioteca.urls', namespace='biblioteca')),
    path('funcionario/', include('funcionario.urls', namespace='funcionario')),
    path('emprestimo/', include('emprestimo.urls', namespace='emprestimo')),
    path('exemplar/', include('exemplar.urls', namespace='exemplar')),
]