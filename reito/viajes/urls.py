from . import views
from django.urls import path

app_name="viajes"

urlpatterns = [
    path('nuevo/', views.NuevoViaje.as_view(), name="nuevo"),
    path('nuevo-destino/', views.NuevoDestino.as_view(), name="nuevo_destino"),
    path('detalle/<int:pk>', views.detalle_viaje, name="detalle"),
    path('editar/<int:pk>', views.EditarViaje.as_view(), name="editar"),
    path('eliminar/<int:pk>', views.EliminarViaje.as_view(), name="eliminar"),
    path('', views.index, name="index"),
    path('detalle-v-viajero/<int:pk>', views.DetalleViajeViajero.as_view(), name="detalle_viaje_viajero"),
    
]
