from django.urls import path
from . import views

app_name = 'vehiculos'

urlpatterns = [
    path('nuevo/', views.VehiculoCrear.as_view(), name='nuevo'),
    path('editar/<int:pk>', views.NuevoVehiculo.as_view(), name='editar'),
    path('eliminar/<int:pk>', views.NuevoVehiculo.as_view(), name='eliminar'),
    path('ver/<int:pk>', views.NuevoVehiculo.as_view(), name='ver'),
]
