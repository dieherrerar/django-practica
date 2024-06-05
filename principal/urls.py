from django.urls import path
from . import views

urlpatterns = [
path('',views.home, name='inicio'),
path('registro/',views.registro, name='registro'),
path('login/', views.iniciar_sesion, name='login')
]
