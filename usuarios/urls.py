from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_usuarios, name='lista_usuarios'),
    path('crear/', views.crear_usuario, name='crear_usuario'),
    path('editar/<int:pk>/', views.editar_usuario, name='editar_usuario'),
    path('eliminar/<int:pk>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('desactivar/<int:pk>/', views.desactivar_usuario, name='desactivar_usuario'),
    path('configuracion/', views.configuracion_cuenta, name='configuracion_cuenta'),
    path('subir_csv/', views.subir_csv, name='subir_csv'),
]
