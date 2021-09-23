from . import views
from django.urls import path

app_name="viajes"

urlpatterns = [
    path('nuevo/', views.NuevoViaje.as_view(), name="nuevo"),
]
