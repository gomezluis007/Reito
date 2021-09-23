from . import views
from django.urls import path

appname="viajes"

urlpatterns = [
    path('', views.index, name="index"),
]
