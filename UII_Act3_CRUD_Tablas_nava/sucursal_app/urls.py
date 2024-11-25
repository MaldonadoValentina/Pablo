from django.urls import path
from sucursal_app import views

urlpatterns = [
    path("sucursal",views.inicio_vistaSucursal, name="sucursal"),
    path("",views.provedor_vista,name="provedor_vista"),
]