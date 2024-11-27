from django.shortcuts import render,redirect
from .models import Sucursal, Provedor

# Create your views here.

def inicio_vista(request):
    lassucursales=Sucursal.objects.all()
    return render(request,"gestionarsucursal.html",{"missucursales":lassucursales})

def provedor_vista(request):
    losprovedores=Provedor.objects.all()
    return render(request,"gestionarsucursal.html",{"misprovedores":losprovedores})