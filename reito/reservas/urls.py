from . import views
from django.urls import path

app_name="reservas"

urlpatterns = [
    path('nueva/<int:user_pk>/<int:viaje_pk>', views.nueva_reserva, name="nueva"),
]