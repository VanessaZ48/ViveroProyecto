from django.db import models

# Modelo Vivero
class Vivero(models.Model):
    finca = models.ForeignKey(Finca, on_delete=models.CASCADE, related_name='viveros')
    codigo = models.CharField(max_length=50, unique=True)  # Asegúrate de que unique=True esté presente
    tipo_cultivo = models.CharField(max_length=100)

    def __str__(self):
        return f'Vivero {self.codigo} - {self.tipo_cultivo}'
    
# Clase abstracta ProductoControl
class ProductoControl(models.Model):
    
    registro_ica = models.CharField(max_length=50)
    nombre_producto = models.CharField(max_length=100)
    frecuencia_aplicacion = models.IntegerField()  # Cada X días
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        abstract = True

# Modelo ProductoControlHongo
class ProductoControlHongo(ProductoControl):
    
    periodo_carencia = models.IntegerField()  # Días
    nombre_hongo = models.CharField(max_length=100)

    def __str__(self):
        return f'Hongo {self.nombre_hongo} - {self.nombre_producto}'