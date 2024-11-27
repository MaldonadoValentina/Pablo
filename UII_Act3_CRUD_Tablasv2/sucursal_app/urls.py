from django.urls import path
from sucursal_app import views

urlpatterns = [
    path("",views.inicio_vista, name="inicio_vista"),
    path("",views.provedor_vista,name="provedor_vista"),
]