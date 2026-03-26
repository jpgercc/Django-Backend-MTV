from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'livro'

router = routers.DefaultRouter()
router.register('', views.LivroViewSet, basename='livro')

urlpatterns = [
    path('', include(router.urls) )
]
