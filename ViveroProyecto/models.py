from django.db import models

# Modelo Vivero
class Vivero(models.Model):
    finca = models.ForeignKey(Finca, on_delete=models.CASCADE, related_name='viveros')
    codigo = models.CharField(max_length=50, unique=True)  # Asegúrate de que unique=True esté presente
    tipo_cultivo = models.CharField(max_length=100)

    def __str__(self):
        return f'Vivero {self.codigo} - {self.tipo_cultivo}'