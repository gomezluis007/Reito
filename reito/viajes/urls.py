from . import views
from django.urls import path

app_name="viajes"

urlpatterns = [
    path('', views.index, name="index"),
]
