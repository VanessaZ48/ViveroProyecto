from django.test import TestCase
from ViveroProyecto.models import Vivero
from django.core.exceptions import ValidationError
from datetime import datetime

# Pruebas para el modelo Vivero
from django.db.utils import IntegrityError

class ViveroTests(TestCase):
    def setUp(self):
        self.finca = Finca.objects.create(
            productor=Productor.objects.create(
                documento_identidad='876543210',
                nombre='Luis',
                apellido='Fernández',
                telefono='5555432',
                correo='luis@example.com'
            ),
            numero_catastro='FNC003',
            municipio='Cali'
        )
        self.vivero = Vivero.objects.create(
            finca=self.finca,
            codigo='VIV002',
            tipo_cultivo='Maíz'
        )
    
    def test_vivero_creation(self):
        """Funcional: Verifica que se pueda crear un Vivero con datos válidos"""
        vivero = Vivero.objects.get(codigo='VIV002')
        self.assertEqual(vivero.tipo_cultivo, 'Maíz')

    def test_vivero_foreign_key(self):
        """Funcional: Verifica que el Vivero esté asociado correctamente a una Finca"""
        self.assertEqual(self.vivero.finca.numero_catastro, 'FNC003')

    def test_vivero_unique_codigo(self):
        """No funcional: Verifica que el código del Vivero sea único"""
        # Primero, crea un Vivero con un código específico
        Vivero.objects.create(
            finca=self.finca,
            codigo='VIV003',
            tipo_cultivo='Trigo'
        )

        # Intenta crear otro Vivero con el mismo código
        try:
            Vivero.objects.create(
                finca=self.finca,
                codigo='VIV003',  # Código duplicado
                tipo_cultivo='Cebada'
            )
            # Si no se lanza una excepción, la prueba falla
            self.fail("Expected IntegrityError due to unique constraint on 'codigo'")
        except IntegrityError:
            pass  # La excepción esperada se ha lanzado

    