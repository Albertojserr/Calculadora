# Cargamos el módulo unittest
import unittest
import sys
sys.path.insert(1,'/home/alberto/Documentos/UAX/Curso 3/Desarrollo Orientado a Objetos/calcu/calculadora-tdd-01-empezamos/src')
from calculadora import Calculator
# Creamos una clase heredando de TestCase
class TestMyCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    def test_initial_value(self):
        self.assertEqual(0, self.calc.value)
# Creamos un nuevo test para comprobar una suma
    def test_add_method(self):
        # Ejecutamos el método
        self.calc.add(1, 3)
        # Comprobamos si el valor es el que esperamos
        self.assertEqual(4, self.calc.value)
# Creamos un nuevo test para comprobar una resta
    def test_min_method(self):
        # Ejecutamos el método
        self.calc.min(3, 1)
        # Comprobamos si el valor es el que esperamos
        self.assertEqual(2, self.calc.value)
# Creamos un nuevo test para comprobar una multiplicación
    def test_plus_method(self):
        # Ejecutamos el método
        self.calc.plus(2, 3)
        # Comprobamos si el valor es el que esperamos
        self.assertEqual(6, self.calc.value)
# Creamos un nuevo test para comprobar una división
    def test_div_method(self):
        # Ejecutamos el método
        self.calc.div(6, 3)
        # Comprobamos si el valor es el que esperamos
        self.assertEqual(2, self.calc.value)
# Creamos un nuevo test para comprobar un factorial
    def test_factorial_method(self):
        # Ejecutamos el método
        self.calc.factorial(3)
        # Comprobamos si el valor es el que esperamos
        self.assertEqual(6, self.calc.value)
# Creamos un nuevo test para comprobar un factorial de 0
    def test_factorial_0_method(self):
        # Ejecutamos el método
        self.calc.factorial(0)
        # Comprobamos si el valor es el que esperamos
        self.assertEqual(1, self.calc.value)
# Creamos un nuevo test para comprobar un factorial de un número negativo
    def test_factorial_neg_method(self):
        # Ejecutamos el método
        self.calc.factorial(-1)
        # Comprobamos si el valor es el que esperamos
        self.assertEqual("No se puede hacer un factorial de un número negativo", self.calc.value)