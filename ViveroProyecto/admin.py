from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Productor, Finca

@admin.register(Productor)
class ProductorAdmin(admin.ModelAdmin):
    list_display = ('documento_identidad', 'nombre', 'apellido', 'telefono', 'correo')

@admin.register(Finca)
class FincaAdmin(admin.ModelAdmin):
    list_display = ('productor', 'numero_catastro', 'municipio')   