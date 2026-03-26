from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'exemplar'

router = routers.DefaultRouter()
router.register('', views.ExemplarViewSet, basename='exemplar')

urlpatterns = [
    path('', include(router.urls) )
]