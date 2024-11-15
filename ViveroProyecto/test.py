from django.test import TestCase
from ViveroProyecto.models import Productor
from django.core.exceptions import ValidationError
from datetime import datetime

# Create your tests here.


"""PRUEBAS CADA ENTIDAD, REQUERIMIENTO FUNCIONALES Y NO FUNCIONALES."""

# Pruebas para el modelo Productor
class ProductorTests(TestCase):
    def setUp(self):
        self.productor = Productor.objects.create(
            documento_identidad='123456789',
            nombre='Juan',
            apellido='Pérez',
            telefono='5551234',
            correo='juan@example.com'
        )
    
    def test_productor_creation(self):
        """Funcional: Verifica que se pueda crear un Productor con datos válidos"""
        productor = Productor.objects.get(documento_identidad='123456789')
        self.assertEqual(productor.nombre, 'Juan')
        self.assertEqual(productor.apellido, 'Pérez')

    def test_productor_unique_documento(self):
        """No funcional: Verifica que el documento de identidad sea único"""
        with self.assertRaises(ValidationError):
            productor = Productor(
                documento_identidad='123456789',
                nombre='Ana',
                apellido='García',
                telefono='5556789',
                correo='ana@example.com'
            )
            productor.full_clean()  # Esto valida los datos y debe fallar

    def test_productor_str_method(self):
        """Funcional: Verifica la representación en cadena del Productor"""
        self.assertEqual(str(self.productor), 'Juan Pérez')
