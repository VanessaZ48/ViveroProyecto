from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Productor, Finca, Vivero, ProductoControlHongo, ProductoControlPlaga

@admin.register(Vivero)
class ViveroAdmin(admin.ModelAdmin):
    list_display = ('finca', 'codigo', 'tipo_cultivo')

@admin.register(ProductoControlHongo)
class ProductoControlHongoAdmin(admin.ModelAdmin):
    list_display = ('registro_ica', 'nombre_producto', 'frecuencia_aplicacion', 'valor', 'periodo_carencia', 'nombre_hongo')

@admin.register(ProductoControlPlaga)
class ProductoControlPlagaAdmin(admin.ModelAdmin):
    list_display = ('registro_ica', 'nombre_producto', 'frecuencia_aplicacion', 'valor', 'periodo_carencia')