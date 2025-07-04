# catalogo/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('quienes-somos/', views.quienes_somos, name='quienes_somos'),
]   