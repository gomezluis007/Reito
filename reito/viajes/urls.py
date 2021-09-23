from . import views
from django.urls import path

app_name="viajes"

urlpatterns = [
    path('nuevo/', views.NuevoViaje.as_view(), name="nuevo"),
    path('nuevo-destino/', views.NuevoDestino.as_view(), name="nuevo_destino"),
    path('detalle/', views.DetalleViaje.as_view(), name="detalle"),
    path('editar/', views.EditarViaje.as_view(), name="editar"),
    path('eliminar/', views.EliminarViaje.as_view(), name="eliminar"),
    path('', views.index, name="index"),
    
]
