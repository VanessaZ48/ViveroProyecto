from django.contrib import admin

@admin.register(Vivero)
class ViveroAdmin(admin.ModelAdmin):
    list_display = ('finca', 'codigo', 'tipo_cultivo')

