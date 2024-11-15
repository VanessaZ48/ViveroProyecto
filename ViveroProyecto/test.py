from django.test import TestCase
from ViveroProyecto.models import Vivero, ProductoControlHongo
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

# Pruebas para el modelo ProductoControlHongo
class ProductoControlHongoTests(TestCase):
    def setUp(self):
        self.producto_hongo = ProductoControlHongo.objects.create(
            registro_ica='ICA456',
            nombre_producto='Fungicida Y',
            frecuencia_aplicacion=30,
            valor=200.00,
            periodo_carencia=10,
            nombre_hongo='Mildiu'
        )

    def test_producto_control_hongo_creation(self):
        """Funcional: Verifica que se pueda crear un ProductoControlHongo con datos válidos"""
        producto = ProductoControlHongo.objects.get(registro_ica='ICA456')
        self.assertEqual(producto.nombre_hongo, 'Mildiu')

    def test_producto_control_hongo_str_method(self):
        """Funcional: Verifica la representación en cadena del ProductoControlHongo"""
        self.assertEqual(str(self.producto_hongo), 'Hongo Mildiu - Fungicida Y')

    def test_producto_control_hongo_periodo_carencia(self):
        """No funcional: Verifica que el periodo de carencia sea un valor entero"""
        self.assertIsInstance(self.producto_hongo.periodo_carencia, int)

    def test_producto_control_hongo_frecuencia_aplicacion(self):
        """No funcional: Verifica que la frecuencia de aplicación sea un valor entero"""
        self.assertIsInstance(self.producto_hongo.frecuencia_aplicacion, int)