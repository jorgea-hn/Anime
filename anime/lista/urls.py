from django.urls import path
from . import views

urlpatterns = [
    path('pendiente/', views.pendientes, name='pendiente'),
    path('vistos/', views.vistos, name='vistos'),
    path('form/', views.form, name='form'),
]
