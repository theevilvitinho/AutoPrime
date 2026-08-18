from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('veiculos/', views.veiculo_list, name='veiculo_list'),
    path('veiculos/novo/', views.veiculo_create, name='veiculo_create'),
    path('veiculos/<int:pk>/editar/', views.veiculo_update, name='veiculo_update'),
    path('veiculos/<int:pk>/excluir/', views.veiculo_delete, name='veiculo_delete'),
    path('veiculos/consulta/', views.veiculo_consulta, name='veiculo_consulta'),
]