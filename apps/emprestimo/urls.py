from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'emprestimo'

router = routers.DefaultRouter()
router.register('', views.EmprestimoViewSet, basename='emprestimo')

urlpatterns = [
    path('', include(router.urls) )
]