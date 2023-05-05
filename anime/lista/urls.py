from django.urls import path
from . import views

app_name = 'lista'

urlpatterns = [
    path('pendiente/', views.pendientes, name='pendiente'),
    path('vistos/', views.vistos, name='vistos'),
    path('form/', views.form, name='form'),
    path('guardar_anime/', views.guardar_anime, name='guardar_anime'),
    path('pendiente/eliminar_anime/<int:tarjeta_id>/<str:vista>/', views.eliminar_anime, name='eliminar_anime'),
    path('editar_anime/<int:anime_id>/', views.editar_anime, name='editar_anime'),
    path('modificar_anime/<int:anime_id>/', views.modificar_anime, name='modificar_anime'),

]
