from . import views
from django.urls import path

appname="usuarios"

urlpatterns = [
    path('signup/', views.NuevoUsuario.as_view(), name="signup"),
    path('login/',views.LoginUsuario.as_view(),name='login'),
]
