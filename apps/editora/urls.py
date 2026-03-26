from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'editora'

router = routers.DefaultRouter()
router.register('', views.EditoraViewSet, basename='editora')

urlpatterns = [
    path('', include(router.urls) )
]
