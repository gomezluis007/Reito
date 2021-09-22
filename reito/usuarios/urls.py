from . import views
from django.urls import path

appname="usuarios"

urlpatterns = [
    path('signup/', views.NuevoUsuario.as_view(), name="signup"),
]
